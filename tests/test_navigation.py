from pages.main_page import MainPage
from playwright.sync_api import expect


def test_about_navigation(page):
    main = MainPage(page)
    main.open()
    main.go_to_about()
    expect(page).to_have_url("https://www.effective-mobile.ru/#about")


def test_jobs_navigation(page):
    main = MainPage(page)
    main.open()
    main.go_to_jobs()
    expect(page).to_have_url("https://www.effective-mobile.ru/#specializations")


def test_reviews_navigation(page):
    main = MainPage(page)
    main.open()
    main.go_to_reviews()
    expect(page).to_have_url("https://www.effective-mobile.ru/#testimonials")


def test_contacts_navigation(page):
    main = MainPage(page)
    main.open()
    main.go_to_contacts()
    expect(page).to_have_url("https://www.effective-mobile.ru/#contact")