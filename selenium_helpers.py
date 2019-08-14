def select(driver,query):
    return driver.find_elements_by_css_selector(query)

def scroll_to_bottom(driver,el):
    driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)",el)

def get_parent(element,parent_element_tag_name):
    parent_element = element.find_element_by_xpath(".//ancestor::{}".format(parent_element_tag_name))
    return parent_element