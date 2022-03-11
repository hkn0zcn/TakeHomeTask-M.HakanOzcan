import time
import pytest
from selenium import webdriver
from pageObjects.wikipage import wikipage

class Test_wikiPage:
    baseURL = "https://en.wikipedia.org/w/index.php?search"
    searchItem = "Adjust"
    textItem = "Adjust"
    notthisitem = "test"
    categoryTemplateItem = "life"

    def test_wikiPageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Search - Wikipedia":
            assert True
        else:
            assert False

    def test_clickSearch(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wikisearchpage = wikipage(self.driver)
        self.wikisearchpage.setSearchItem(self.searchItem)
        self.wikisearchpage.clickSearchButton()
        act_title =self.driver.title
        self.wikisearchpage.checkSearchResultsExist()
        self.driver.close()
        if act_title == "Adjust - Search results - Wikipedia":
            assert True
        else:
            assert False

    def test_advanceSearchBar(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wikisearchpage = wikipage(self.driver)
        time.sleep(1)
        self.wikisearchpage.clickAdvanceSearchBar()
        self.wikisearchpage.checkAdvanceSearchOptionsScreen()
        self.driver.close()

    def test_searchInBar(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wikisearchpage = wikipage(self.driver)
        time.sleep(1)
        self.wikisearchpage.clickSearchInBar()
        self.wikisearchpage.checkSearchInBarScreen()
        self.driver.close()

    def test_advanceSearhBarFields(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wikisearchpage = wikipage(self.driver)
        self.wikisearchpage.setSearchItem(self.searchItem)
        time.sleep(1)
        self.wikisearchpage.clickAdvanceSearchBar()
        self.wikisearchpage.setTheseWordsItem(self.textItem)
        self.wikisearchpage.setExactlyThisTextItem(self.textItem)
        self.wikisearchpage.setNotTheseWordsItem(self.notthisitem)
        self.wikisearchpage.setoneOfTheseWordsItem(self.textItem)
        self.wikisearchpage.setpageTitleContainsItem(self.textItem)
        self.wikisearchpage.setsubPageofThisPageItem(self.textItem)
        self.wikisearchpage.setpagesInThisCategoryItem(self.categoryTemplateItem)
        self.wikisearchpage.setpagesWithThisTemplatesItem(self.categoryTemplateItem)
        self.wikisearchpage.clickSortingOrder()
        self.wikisearchpage.clickSortingOrderCreationDate()
        self.wikisearchpage.clickSearchButton()
        self.wikisearchpage.checkaWarningSearchScreen()
        self.driver.close()

    def test_searchInBarFields(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wikisearchpage = wikipage(self.driver)
        self.wikisearchpage.setSearchItem(self.searchItem)
        time.sleep(1)
        self.wikisearchpage.clickSearchInBar()
        self.wikisearchpage.clickSearchInBarDefault()
        self.wikisearchpage.clickSearchInBarDiscussion()
        self.wikisearchpage.clickSearchInBarGeneralHelp()
        self.wikisearchpage.clickSearchInBarAll()
        self.wikisearchpage.clickSearchButton()
        self.wikisearchpage.checkGadgetDefinition()
        self.driver.close()

    def test_SearchWithEnterButton(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wikisearchpage = wikipage(self.driver)
        self.wikisearchpage.setSearchItem(self.searchItem)
        self.wikisearchpage.sendKeyEnter()
        act_title = self.driver.title
        self.wikisearchpage.checkSearchResultsExist()
        self.driver.close()
        if act_title == "Adjust - Search results - Wikipedia":
            assert True
        else:
            assert False
