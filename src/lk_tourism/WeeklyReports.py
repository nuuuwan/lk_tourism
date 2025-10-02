from typing import Generator

from scraper import AbstractPDFDoc


class WeeklyReports(AbstractPDFDoc):
    @classmethod
    def doc_class_label(cls):
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
    def gen_docs(cls) -> Generator["WeeklyReports", None, None]:
        return
