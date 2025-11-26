*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser To Home Page
Suite Teardown    Close Browser
Test Setup        Go To Home Page

*** Variables ***
${SERVER}         localhost:5000
${BROWSER}        headlesschrome
${DELAY}          0
${HOME URL}       http://${SERVER}/

*** Keywords ***
Open Browser To Home Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    Call Method    ${options}    add_argument    --disable-gpu
    Open Browser    ${HOME URL}    ${BROWSER}    options=${options}
    Set Selenium Speed    ${DELAY}

Go To Home Page
    Go To    ${HOME URL}
    Title Should Be    Varasto - Etusivu

*** Test Cases ***
Home Page Should Show Title
    Page Should Contain    Varastonhallinta

Home Page Should Have Create Warehouse Link
    Page Should Contain Link    Luo uusi varasto

Home Page Should Show Empty Message When No Warehouses
    Page Should Contain    Ei varastoja

Create New Warehouse
    Click Link    Luo uusi varasto
    Title Should Be    Luo uusi varasto
    Input Text    nimi    Mehuvarasto
    Input Text    tilavuus    100.0
    Input Text    alku_saldo    20.0
    Click Button    Luo varasto
    Title Should Be    Varasto - Etusivu
    Page Should Contain    Mehuvarasto
    Page Should Contain    100.00
    Page Should Contain    20.00
    Page Should Contain    80.00

View Warehouse Details
    Click Link    Luo uusi varasto
    Input Text    nimi    Olutvarasto
    Input Text    tilavuus    50.0
    Input Text    alku_saldo    10.0
    Click Button    Luo varasto
    Click Element    xpath=//a[@class='view-btn'][last()]
    Title Should Contain    Olutvarasto
    Page Should Contain    Tilavuus:
    Page Should Contain    50.00
    Page Should Contain    Saldo:
    Page Should Contain    10.00
    Page Should Contain    Vapaa tila:
    Page Should Contain    40.00

Add Items To Warehouse
    Click Link    Luo uusi varasto
    Input Text    nimi    Testivarasto
    Input Text    tilavuus    100.0
    Input Text    alku_saldo    20.0
    Click Button    Luo varasto
    Click Element    xpath=//a[@class='view-btn'][last()]
    Input Text    lisaa_maara    30.5
    Click Button    Lisää
    Page Should Contain    50.50

Remove Items From Warehouse
    Click Link    Luo uusi varasto
    Input Text    nimi    Ottovarasto
    Input Text    tilavuus    100.0
    Input Text    alku_saldo    50.0
    Click Button    Luo varasto
    Click Element    xpath=//a[@class='view-btn'][last()]
    Input Text    ota_maara    15.5
    Click Button    Ota
    Page Should Contain    34.50

Create Multiple Warehouses
    Click Link    Luo uusi varasto
    Input Text    nimi    Varasto1
    Input Text    tilavuus    100.0
    Click Button    Luo varasto
    Click Link    Luo uusi varasto
    Input Text    nimi    Varasto2
    Input Text    tilavuus    200.0
    Click Button    Luo varasto
    Page Should Contain    Varasto1
    Page Should Contain    Varasto2

Navigate Back From Warehouse Details
    Click Link    Luo uusi varasto
    Input Text    nimi    Paluuvarasto
    Input Text    tilavuus    50.0
    Click Button    Luo varasto
    Click Element    xpath=//a[@class='view-btn'][last()]
    Click Link    ← Takaisin
    Title Should Be    Varasto - Etusivu

Cancel Warehouse Creation
    Click Link    Luo uusi varasto
    Click Link    Peruuta
    Title Should Be    Varasto - Etusivu
