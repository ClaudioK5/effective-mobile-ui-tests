from playwright.sync_api import Page

class MainPage:
    BASE_URL = "https://www.effective-mobile.ru/"

    LINK_ABOUT = "a[href='#about']"
    LINK_JOBS = "a[href='#specializations']"
    LINK_REVIEWS = "a[href='#testimonials']"
    LINK_CONTACTS = "a[href='#contact']"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.BASE_URL)

    def go_to_about(self):
        self.page.click(self.LINK_ABOUT)

    def go_to_jobs(self):
        self.page.click(self.LINK_JOBS)

    def go_to_reviews(self):
        self.page.click(self.LINK_REVIEWS)

    def go_to_contacts(self):
        self.page.click(self.LINK_CONTACTS)