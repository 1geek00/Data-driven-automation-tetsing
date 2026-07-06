import csv
from playwright.sync_api import Page

def get_csv_data():
    data = []
    with open("./data.csv.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def test_login(page: Page):
    data = get_csv_data()

    for row in data:
        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.get_by_role("textbox", name="Username").fill(row["username"])
        page.get_by_role("textbox", name="Password").fill(row["password"])

        page.get_by_role("button", name="Submit").click()

        page.get_by_role("link", name="Log out").click()