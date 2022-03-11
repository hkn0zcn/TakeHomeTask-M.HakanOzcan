from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class wikipage:

    searchbox_id = "ooui-php-1"
    searchbutton_xpath = "//button/span[2]"
    advancesearchbar_xpath = "//div[@class='oo-ui-widget oo-ui-widget-enabled mw-advancedSearch-expandablePane-options']//span[@class='mw-advancedSearch-expandablePane-button oo-ui-widget oo-ui-widget-enabled oo-ui-buttonElement oo-ui-buttonElement-framed oo-ui-indicatorElement oo-ui-labelElement oo-ui-buttonWidget']//span[@class='oo-ui-indicatorElement-indicator oo-ui-indicator-down']"
    searchinbar_xpath = "//div[@class='oo-ui-widget oo-ui-widget-enabled mw-advancedSearch-expandablePane-namespaces']//span[@class='oo-ui-indicatorElement-indicator oo-ui-indicator-down']"
    searchresults_css = ".mw-search-result"
    advancesearchscreen_id = "mw-advancedSearch-expandable-options"
    searchinbarscreen_xpath = "//div[@class='mw-advancedSearch-namespaceFilter oo-ui-widget oo-ui-widget-enabled oo-ui-draggableGroupElement oo-ui-tagMultiselectWidget oo-ui-tagMultiselectWidget-outlined oo-ui-menuTagMultiselectWidget']//div[@class='oo-ui-tagMultiselectWidget-content']"
    thesewords_xpath ="//input[@id='ooui-31']"
    exactlythistext_xpath = "//input[@id='ooui-33']"
    notthesewords_xpath = "//input[@id='ooui-35']"
    oneofthesewords_xpath = "//input[@id='ooui-37']"
    pagetitlecontains_xpath = "//input[@id='ooui-39']"
    subpagesofthispage_xpath = "//input[@id='ooui-41']"
    pagesinthecategory_xpath = "//input[@id='ooui-44']"
    pageswiththistemplates_xpath = "//input[@id='ooui-47']"
    sortingorder_xpath = "/html[1]/body[1]/div[3]/div[3]/div[4]/div[2]/form[1]/div[4]/div[1]/div[1]/div[1]/fieldset[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"
    sortingoredercreationdate_xpath = "//span[contains(text(),'Creation date – current on top')]"
    searchindefault_xpath = "//input[@value='defaultNamespaces']"
    searchindiscussion_xpath = "//input[@value='discussion']"
    searchingeneralhelp_xpath = "//input[@value='generalHelp']"
    searchinall_xpath = "//input[@value='all']"
    awarningsearch_xpath = "//p[contains(text(),'A warning has occurred while searching: Deep categ')]"
    gadgetdefinition_xpath = "/html[1]/body[1]/div[3]/div[3]/div[4]/div[2]/form[1]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[28]/span[1]"

    def __init__(self, driver):
        self.driver = driver

    def setSearchItem(self,searchitem):
        self.driver.find_element_by_id(self.searchbox_id).clear()
        self.driver.find_element_by_id(self.searchbox_id).send_keys(searchitem)

    def setTheseWordsItem(self, textItem):
        self.driver.find_element_by_xpath(self.thesewords_xpath).clear()
        self.driver.find_element_by_xpath(self.thesewords_xpath).send_keys(textItem)

    def setTheseWordsItem(self, textItem):
        self.driver.find_element_by_xpath(self.thesewords_xpath).clear()
        self.driver.find_element_by_xpath(self.thesewords_xpath).send_keys(textItem)

    def setExactlyThisTextItem(self,textItem):
        self.driver.find_element_by_xpath(self.exactlythistext_xpath).clear()
        self.driver.find_element_by_xpath(self.exactlythistext_xpath).send_keys(textItem)

    def setNotTheseWordsItem(self,notthisitem):
        self.driver.find_element_by_xpath(self.notthesewords_xpath).clear()
        self.driver.find_element_by_xpath(self.notthesewords_xpath).send_keys(notthisitem)

    def setoneOfTheseWordsItem(self,textItem):
        self.driver.find_element_by_xpath(self.oneofthesewords_xpath).clear()
        self.driver.find_element_by_xpath(self.oneofthesewords_xpath).send_keys(textItem)
        self.driver.find_element_by_xpath(self.oneofthesewords_xpath).send_keys(textItem)

    def setpageTitleContainsItem(self,textItem):
        self.driver.find_element_by_xpath(self.pagetitlecontains_xpath).clear()
        self.driver.find_element_by_xpath(self.pagetitlecontains_xpath).send_keys(textItem)

    def setsubPageofThisPageItem(self,textItem):
        self.driver.find_element_by_xpath(self.subpagesofthispage_xpath).clear()
        self.driver.find_element_by_xpath(self.subpagesofthispage_xpath).send_keys(textItem)

    def setpagesInThisCategoryItem(self,categoryTemplateItem):
        self.driver.find_element_by_xpath(self.pagesinthecategory_xpath).clear()
        self.driver.find_element_by_xpath(self.pagesinthecategory_xpath).send_keys(categoryTemplateItem)

    def setpagesWithThisTemplatesItem(self,categoryTemplateItem):
        self.driver.find_element_by_xpath(self.pageswiththistemplates_xpath).clear()
        self.driver.find_element_by_xpath(self.pageswiththistemplates_xpath).send_keys(categoryTemplateItem)

    def clickSortingOrder(self):
        self.driver.find_element_by_xpath(self.sortingorder_xpath).click()

    def clickSortingOrderCreationDate(self):
        self.driver.find_element_by_xpath(self.sortingoredercreationdate_xpath).click()

    def clickSearchButton(self):
        self.driver.find_element_by_xpath(self.searchbutton_xpath).click()

    def clickAdvanceSearchBar(self):
        self.driver.find_element_by_xpath(self.advancesearchbar_xpath).click()

    def clickSearchInBar(self):
        self.driver.find_element_by_xpath(self.searchinbar_xpath).click()

    def clickSearchInBarDefault(self):
        self.driver.find_element_by_xpath(self.searchindefault_xpath).click()

    def clickSearchInBarDiscussion(self):
        self.driver.find_element_by_xpath(self.searchindiscussion_xpath).click()

    def clickSearchInBarGeneralHelp(self):
        self.driver.find_element_by_xpath(self.searchingeneralhelp_xpath).click()

    def clickSearchInBarAll(self):
        self.driver.find_element_by_xpath(self.searchinall_xpath).click()

    def checkSearchResultsExist(self):
        try:
            self.driver.find_element_by_css_selector(self.searchresults_css)
        except NoSuchElementException:
            return False
        return True

    def checkAdvanceSearchOptionsScreen(self):
        try:
            self.driver.find_element_by_id(self.advancesearchscreen_id)
        except NoSuchElementException:
            return False
        return True

    def checkSearchInBarScreen(self):
        try:
            self.driver.find_element_by_xpath(self.searchinbarscreen_xpath)
        except NoSuchElementException:
            return False
        return True

    def checkaWarningSearchScreen(self):
        try:
            self.driver.find_element_by_xpath(self.awarningsearch_xpath)
        except NoSuchElementException:
            return False
        return True

    def checkGadgetDefinition(self):
        try:
            self.driver.find_element_by_xpath(self.gadgetdefinition_xpath)
        except NoSuchElementException:
            return False
        return True

    def sendKeyEnter(self):
        self.driver.find_element_by_id(self.searchbox_id).send_keys(Keys.ENTER)


