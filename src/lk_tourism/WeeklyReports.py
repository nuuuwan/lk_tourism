from typing import Generator

from utils import TimeFormat

from scraper import AbstractPDFDoc
from utils_future import WWW


class WeeklyReports(AbstractPDFDoc):
    URL_BASE = "https://www.sltda.gov.lk"

    @classmethod
    def get_doc_class_label(cls):
        return "lk_tourism_weekly_reports"

    @classmethod
    def get_doc_class_description(cls) -> str:
        return "\n\n".join(
            [
                "Report on Weekly Tourist Arrivals to Sri Lanka.",  # noqa: E501
            ]
        )

    @classmethod
    def get_doc_class_emoji(cls) -> str:
        return "🌴"

    @classmethod
    def gen_year_urls(cls):
        url_years = cls.URL_BASE + "/en/weekly-tourist-arrivals-reports-2023"
        www = WWW(url_years)
        soup = www.soup
        assert soup, f"[{www}] Failed to get soup."
        div = soup.find("div", class_="downloads-table")
        assert div, f"[{www}] Failed to find div.downloads-table"
        a_list = div.find_all("a")
        for a in a_list:
            url_for_year = a.get("href")
            yield url_for_year

    @classmethod
    def gen_docs_for_year(cls, url_year):
        www = WWW(url_year)
        soup = www.soup
        assert soup, f"[{www}] Failed to get soup."
        div_items = soup.find_all("div", class_="register-item-back")
        assert len(div_items) > 0, f"[{www}] No div.register-item found."
        for div_item in div_items:
            div_text = div_item.find("div", class_="register-item-text")
            assert div_text, f"[{www}] No div.register-item-text found."
            description = div_text.get_text().strip()
            _, year_text, month_text = description.split("-")
            date_str = TimeFormat.DATE.format(
                TimeFormat("%Y %B").parse(
                    year_text.strip() + " " + month_text.strip().title()
                )
            )
            num = date_str

            a = div_item.find("a")
            assert a, f"[{www}] No <a> found in div.register-item-back"
            url_pdf = a.get("href")
            assert url_pdf.endswith(
                ".pdf"
            ), f"Unexpected non-PDF href: {url_pdf}"

            yield WeeklyReports(
                num=num,
                date_str=date_str,
                url_metadata=url_year,
                description=description,
                lang="en",
                url_pdf=url_pdf,
            )

    @classmethod
    def gen_docs(cls) -> Generator["WeeklyReports", None, None]:
        for url_year in cls.gen_year_urls():
            yield from cls.gen_docs_for_year(url_year)
