class NavbarMenu:
    #catalog_xpath="//a[@class='nav-link']//p[@xpath=1][contains(text(),'Catalog')]"
    catalog_xpath="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon fas fa-book']"
    sales_xpath="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon fas fa-shopping-cart']"
    customer_xpath="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon far fa-user']"
    promotions_xpath="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon fas fa-tags']"
    content_management_xpth="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon fas fa-cubes']"
    configuration_xpath="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon fas fa-cogs']"
    system_xpath="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon fas fa-cube']"
    reports_xpath="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon fas fa-chart-line']"
    help_xpath="//nav[@class='mt-2']//ul[@role='menu']//li//a//i[@class='nav-icon fas fa-question-circle']"

    #all_menu_option_xpath="//nav[@class='mt-2']//ul[@role='menu']//li[@class='nav-item has-treeview']"