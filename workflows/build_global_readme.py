from scraper import GlobalReadMe


def main():
    GlobalReadMe(
        {
            "lk_tourism": [
                "lk_tourism_weekly_reports",
                "lk_tourism_monthly_reports",
            ]
        }
    ).build()


if __name__ == "__main__":
    main()
