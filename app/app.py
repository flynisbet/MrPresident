from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/pres")
def presidentData():
    presidents = {
    "1": {
        "No": "1",
        "Name": " George Washington",
        "Term Years": "1789\u20131797",
        "Vice President": "John Adams",
        "First Lady": "Martha Washington",
        "Party": "None ",
        "Birth-Death ": "February 22, 1732 \u2013 December 14, 1799",
        "IMG filepath": "../asset/img/1_Washington.jpeg",
        "Description": "As the first president, Washington established key precedents, including the formation of a cabinet and the tradition of serving only two terms. He emphasized national unity and neutrality in foreign affairs, steering the nation through its formative years. His leadership set a foundation for the presidency's role in American governance."
    },
    "2": {
        "No": "2",
        "Name": " John Adams",
        "Term Years": "1797\u20131801",
        "Vice President": "Thomas Jefferson",
        "First Lady": "Abigail Adams",
        "Party": "Federalist",
        "Birth-Death ": "October 30, 1735 \u2013 July 4, 1826",
        "IMG filepath": "../asset/img/2_Adams.jpeg",
        "Description": "Adams focused on foreign affairs, particularly tensions with France, and signed the controversial Alien and Sedition Acts, which limited immigration and curtailed free speech. His presidency faced significant challenges, including political division and conflicts with Congress. Despite his efforts to maintain peace, he struggled with the growing partisanship of the time."
    },
    "3": {
        "No": "3",
        "Name": " Thomas Jefferson",
        "Term Years": "1801\u20131809",
        "Vice President": "Aaron Burr, George Clinton",
        "First Lady": "Martha Jefferson(daughter)",
        "Party": "Democratic-Republican",
        "Birth-Death ": "April 13, 1743 \u2013 July 4, 1826",
        "IMG filepath": "../asset/img/3_Jefferson.jpeg",
        "Description": "Jefferson championed limited government and individual liberties, overseeing the Louisiana Purchase, which doubled the size of the United States. He sought to promote agrarianism and reduce federal power, emphasizing the importance of states\u2019 rights. His presidency also faced challenges in foreign relations, particularly with Britain and France."
    },
    "4": {
        "No": "4",
        "Name": " James Madison",
        "Term Years": "1809\u20131817",
        "Vice President": "George Clinton, Elbridge Gerry",
        "First Lady": "Dolley Madison",
        "Party": "Democratic-Republican",
        "Birth-Death ": "March 16, 1751 \u2013 June 28, 1836",
        "IMG filepath": "../asset/img/4_Madison.jpeg",
        "Description": "Madison, known as the \"Father of the Constitution,\" led the nation during the War of 1812 against Britain, which tested American sovereignty. His administration faced domestic challenges, including economic struggles and political opposition. The war ultimately bolstered national unity and the sense of American identity."
    },
    "5": {
        "No": "5",
        "Name": " James Monroe",
        "Term Years": "1817\u20131825",
        "Vice President": "Daniel D. Tompkins",
        "First Lady": "Elizabeth Monroe",
        "Party": "Democratic-Republican",
        "Birth-Death ": "April 28, 1758 \u2013 July 4, 1831",
        "IMG filepath": "../asset/img/5_Monroe.jpeg",
        "Description": "Monroe's presidency is noted for the Monroe Doctrine, asserting U.S. opposition to European colonization in the Americas. He promoted westward expansion and national unity during the \"Era of Good Feelings.\" His administration navigated both domestic growth and foreign relations with increasing assertiveness."
    },
    "6": {
        "No": "6",
        "Name": " John Quincy Adams",
        "Term Years": "1825\u20131829",
        "Vice President": "John C. Calhoun",
        "First Lady": "Louisa Adams",
        "Party": "Democratic-Republican",
        "Birth-Death ": "July 11, 1767 \u2013 February 23, 1848",
        "IMG filepath": "../asset/img/6_Adams.jpeg",
        "Description": "Adams advocated for ambitious internal improvements and a strong federal role in economic development but faced significant opposition from the Jacksonian Democrats. His presidency was marred by political infighting and accusations of corruption. Despite his vision, he struggled to implement his policies effectively."
    },
    "7": {
        "No": "7",
        "Name": " Andrew Jackson",
        "Term Years": "1829\u20131837",
        "Vice President": "John C. Calhoun, Martin Van Buren",
        "First Lady": "Emily Donelson, Sarah Jackson",
        "Party": "Democratic",
        "Birth-Death ": "March 15, 1767 \u2013 June 8, 1845",
        "IMG filepath": "../asset/img/7_Jackson.jpeg",
        "Description": "Jackson's presidency emphasized the \"common man,\" as he expanded democratic participation and implemented the Indian Removal Act. He faced criticism for his opposition to the Second Bank of the United States, which he viewed as a corrupt institution. His leadership marked a significant shift toward populism in American politics."
    },
    "8": {
        "No": "8",
        "Name": " Martin Van Buren",
        "Term Years": "1837\u20131841",
        "Vice President": "Richard Mentor Johnson",
        "First Lady": "Sarah Van Buren",
        "Party": "Democratic",
        "Birth-Death ": "December 5, 1782 \u2013 July 24, 1862",
        "IMG filepath": "../asset/img/8_VanBuren.jpeg",
        "Description": "Van Buren's presidency was overshadowed by the Panic of 1837, a major economic depression that led to widespread unemployment and hardship. He sought to maintain party loyalty and navigate the economic crisis, though his efforts were often met with frustration. His term highlighted the challenges of governance amid economic turmoil."
    },
    "9": {
        "No": "9",
        "Name": " William Henry Harrison",
        "Term Years": "1841",
        "Vice President": "John Tyler",
        "First Lady": "Anna Harrison",
        "Party": "Whig",
        "Birth-Death ": "February 9, 1773 \u2013 April 4, 1841",
        "IMG filepath": "../asset/img/9_Harrison.jpeg",
        "Description": "Harrison served the shortest presidency in U.S. history, dying just weeks after his inauguration. His death raised significant questions about presidential succession and the powers of the vice president. Despite his brief term, he became a symbol of the emerging Whig Party"
    },
    "10": {
        "No": "10",
        "Name": " John Tyler",
        "Term Years": "1841\u20131845",
        "Vice President": "None",
        "First Lady": "Letitia Tyler, Julia Tyler",
        "Party": "Whig ",
        "Birth-Death ": "March 29, 1790 \u2013 January 18, 1862",
        "IMG filepath": "../asset/img/10_Tyler.jpeg",
        "Description": "yler, who assumed the presidency after Harrison's death, faced significant opposition from his own party and struggled to enact his agenda. He championed westward expansion and the annexation of Texas, but his presidency was marred by political strife. Tyler's actions set the stage for future territorial conflicts."
    },
    "11": {
        "No": "11",
        "Name": " James K. Polk",
        "Term Years": "1845\u20131849",
        "Vice President": "George M. Dallas",
        "First Lady": "Sarah Polk",
        "Party": "Democratic",
        "Birth-Death ": "November 2, 1795 \u2013 June 15, 1849",
        "IMG filepath": "../asset/img/11_Polk.jpeg",
        "Description": "Polk aggressively promoted Manifest Destiny, leading the nation through the Mexican-American War, which resulted in significant territorial gains. He focused on expanding U.S. territory and enhancing the nation's economic strength. His administration is often regarded as one of the most effective in pursuing a clear agenda."
    },
    "12": {
        "No": "12",
        "Name": " Zachary Taylor",
        "Term Years": "1849\u20131850",
        "Vice President": "Millard Fillmore",
        "First Lady": "Margaret Taylor",
        "Party": "Whig",
        "Birth-Death ": "November 24, 1784 \u2013 July 9, 1850",
        "IMG filepath": "../asset/img/12_Taylor.jpeg",
        "Description": "Taylor's presidency focused on national unity amid rising tensions over slavery in the newly acquired territories. He advocated for a compromise on the issue but died unexpectedly after just 16 months in office. His death left unresolved debates that would later escalate into civil conflict."
    },
    "13": {
        "No": "13",
        "Name": " Millard Fillmore",
        "Term Years": "1850\u20131853",
        "Vice President": "None",
        "First Lady": "Abigail Fillmore",
        "Party": "Whig ",
        "Birth-Death ": "January 7, 1800 \u2013 March 8, 1874",
        "IMG filepath": "../asset/img/13_Fillmore.jpeg",
        "Description": "Fillmore supported the Compromise of 1850, which sought to ease tensions between free and slave states but ultimately heightened sectional conflict. His administration struggled with the divisive issue of slavery, which dominated national politics. Fillmore's failure to find lasting solutions contributed to the growing divide."
    },
    "14": {
        "No": "14",
        "Name": " Franklin Pierce",
        "Term Years": "1853\u20131857",
        "Vice President": "William R. King",
        "First Lady": "Jane Pierce",
        "Party": "Democratic",
        "Birth-Death ": "November 23, 1804 \u2013 October 8, 1869",
        "IMG filepath": "../asset/img/14_Pierce.jpeg",
        "Description": "Pierce's presidency was marked by the controversial Kansas-Nebraska Act, which allowed new territories to decide on slavery, leading to violent conflicts known as \"Bleeding Kansas.\" He aimed to expand U.S. territory but faced criticism for his handling of the growing sectional tensions. His administration's inability to unite the nation deepened divisions."
    },
    "15": {
        "No": "15",
        "Name": " James Buchanan",
        "Term Years": "1857\u20131861",
        "Vice President": "John C. Breckinridge",
        "First Lady": "Harriet Lane",
        "Party": "Democratic",
        "Birth-Death ": "April 23, 1791 \u2013 June 1, 1868",
        "IMG filepath": "../asset/img/15_Buchanan.jpeg",
        "Description": "Buchanan's presidency was characterized by his ineffective response to the secession crisis as tensions over slavery escalated. He believed in a limited federal role, which left him unable to address the mounting conflicts between North and South. His inaction and perceived favoritism toward slave states alienated many Americans."
    },
    "16": {
        "No": "16",
        "Name": " Abraham Lincoln",
        "Term Years": "1861\u20131865",
        "Vice President": "Hannibal Hamlin, Andrew Johnson",
        "First Lady": "Mary Lincoln",
        "Party": "Republican",
        "Birth-Death ": "February 12, 1809 \u2013 April 15, 1865",
        "IMG filepath": "../asset/img/16_Lincoln.jpeg",
        "Description": "Lincoln led the nation through the Civil War, emphasizing the preservation of the Union and the abolition of slavery. He issued the Emancipation Proclamation, which transformed the war's purpose and advanced civil rights. His leadership and vision for reconciliation were cut short by his assassination in 1865."
    },
    "17": {
        "No": "17",
        "Name": " Andrew Johnson",
        "Term Years": "1865\u20131869",
        "Vice President": "None",
        "First Lady": "Eliza Johnson",
        "Party": "National Union",
        "Birth-Death ": "December 29, 1808 \u2013 July 31, 1875",
        "IMG filepath": "../asset/img/17_Johnson.jpeg",
        "Description": "Johnson's presidency faced intense challenges during Reconstruction as he attempted to implement his vision for the South's reintegration. His lenient policies toward former Confederates angered many in Congress, leading to his impeachment. Though acquitted, his presidency was marked by conflict and ineffective governance."
    },
    "18": {
        "No": "18",
        "Name": " Ulysses S. Grant",
        "Term Years": "1869\u20131877",
        "Vice President": "Schuyler Colfax, Henry Wilson",
        "First Lady": "Julia Grant",
        "Party": "Republican",
        "Birth-Death ": "April 27, 1822 \u2013 July 23, 1885",
        "IMG filepath": "../asset/img/18_Grant.jpeg",
        "Description": "Grant focused on Reconstruction and civil rights but faced significant corruption scandals within his administration. He championed the enforcement of civil rights laws and worked to protect the rights of freedmen. Despite his military successes, his presidency was marred by political turmoil."
    },
    "19": {
        "No": "19",
        "Name": " Rutherford B. Hayes",
        "Term Years": "1877\u20131881",
        "Vice President": "William A. Wheeler",
        "First Lady": "Lucy Hayes",
        "Party": "Republican",
        "Birth-Death ": "October 4, 1822 \u2013 January 17, 1893",
        "IMG filepath": "../asset/img/19_Hayes.jpeg",
        "Description": "Hayes sought to restore public trust in government following the scandals of the Grant administration and emphasized civil service reform. His presidency marked the end of Reconstruction and the withdrawal of federal troops from the South. He faced challenges in uniting a divided nation and navigating economic issues."
    },
    "20": {
        "No": "20",
        "Name": " James A. Garfield",
        "Term Years": "1881",
        "Vice President": "Chester A. Arthur",
        "First Lady": "Lucrieta Garfield",
        "Party": "Republican",
        "Birth-Death ": "November 19, 1831 \u2013 September 19, 1881",
        "IMG filepath": "../asset/img/20_Garfield.jpeg",
        "Description": "Garfield advocated for civil service reform and economic modernization but was assassinated just months into his term. His presidency was cut short, but his vision for government reform left a lasting impact. His death led to significant changes in how political appointments were handled."
    },
    "21": {
        "No": "21",
        "Name": " Chester A. Arthur",
        "Term Years": "1881\u20131885",
        "Vice President": "None",
        "First Lady": "Mary McElroy",
        "Party": "Republican",
        "Birth-Death ": "October 5, 1829 \u2013 November 18, 1886",
        "IMG filepath": "../asset/img/21_Arthur.jpeg",
        "Description": "Arthur continued Garfield's push for civil service reform and successfully signed the Pendleton Act, which established a merit-based system for federal hiring. His presidency focused on modernization and infrastructure development. Despite initial skepticism, he gained respect for his efforts to improve government integrity."
    },
    "22": {
        "No": "22",
        "Name": " Grover Cleveland",
        "Term Years": "1885\u20131889",
        "Vice President": "Thomas A. Hendricks",
        "First Lady": "Rose Cleveland, Frances Cleveland",
        "Party": "Democratic",
        "Birth-Death ": "March 18, 1837 \u2013 June 24, 1908",
        "IMG filepath": "../asset/img/22_Cleveland.jpeg",
        "Description": "Cleveland's presidency was marked by his commitment to political reform and economic conservatism, focusing on reducing tariffs and government waste. He faced significant opposition from the Republican Party and dealt with labor unrest and economic issues. His return to the presidency for a non-consecutive second term underscored his political resilience."
    },
    "23": {
        "No": "23",
        "Name": " Benjamin Harrison",
        "Term Years": "1889\u20131893",
        "Vice President": "Levi P. Morton",
        "First Lady": "Caroline Harrison, Mary Harrison McKee",
        "Party": "Republican",
        "Birth-Death ": "August 20, 1833 \u2013 March 13, 1901",
        "IMG filepath": "../asset/img/23_Harrison.jpeg",
        "Description": "Harrison's presidency focused on high tariffs and the expansion of the Navy, overseeing the admission of six new states. He advocated for civil rights for African Americans but faced challenges implementing his agenda. His administration is often remembered for its active foreign policy."
    },
    "24": {
        "No": "24",
        "Name": " Grover Cleveland",
        "Term Years": "1893\u20131897",
        "Vice President": "Adlai Stevenson I",
        "First Lady": "Frances Cleveland",
        "Party": "Democratic ",
        "Birth-Death ": "March 18, 1837 \u2013 June 24, 1908",
        "IMG filepath": "../asset/img/24_Cleveland.jpeg",
        "Description": "Cleveland returned to the presidency amid economic turmoil, addressing the Panic of 1893 with a focus on maintaining a gold standard. He emphasized fiscal conservatism and sought to limit federal intervention in the economy. His second term was marked by significant labor strikes and conflicts with business interests."
    },
    "25": {
        "No": "25",
        "Name": " William McKinley",
        "Term Years": "1897\u20131901",
        "Vice President": "Garret A. Hobart, Theodore Roosevelt",
        "First Lady": "Ida McKinley",
        "Party": "Republican",
        "Birth-Death ": "January 29, 1843 \u2013 September 14, 1901",
        "IMG filepath": "../asset/img/25_McKinley.jpeg",
        "Description": "McKinley's presidency is noted for its economic prosperity and the Spanish-American War, which established the U.S. as a global power. He promoted protective tariffs and sought to maintain a balanced budget. His assassination in 1901 cut short his efforts to address domestic and foreign challenges."
    },
    "26": {
        "No": "26",
        "Name": " Theodore Roosevelt",
        "Term Years": "1901\u20131909",
        "Vice President": "Charles W. Fairbanks",
        "First Lady": "Edith Roosevelt",
        "Party": "Republican",
        "Birth-Death ": "October 27, 1858 \u2013 January 6, 1919",
        "IMG filepath": "../asset/img/26_Roosevelt.jpeg",
        "Description": "Roosevelt championed progressive reforms, including trust-busting, conservation efforts, and consumer protection. His energetic leadership transformed the presidency into a more active and visible role in American life. He also pursued an assertive foreign policy, exemplified by the construction of the Panama Canal."
    },
    "27": {
        "No": "27",
        "Name": " William Howard Taft",
        "Term Years": "1909\u20131913",
        "Vice President": "James S. Sherman",
        "First Lady": "Helen Taft",
        "Party": "Republican",
        "Birth-Death ": "September 15, 1857 \u2013 March 8, 1930",
        "IMG filepath": "../asset/img/27_Taft.jpeg",
        "Description": "Taft continued progressive reforms but faced criticism for his support of tariff increases and perceived betrayal of Roosevelt's vision. He emphasized trust-busting and maintained a focus on foreign policy, particularly in Latin America. His presidency highlighted divisions within the Republican Party, leading to a split in the 1912 election."
    },
    "28": {
        "No": "28",
        "Name": " Woodrow Wilson",
        "Term Years": "1913\u20131921",
        "Vice President": "Thomas R. Marshall",
        "First Lady": "Ellen Wilson, Edith Wilson",
        "Party": "Democratic",
        "Birth-Death ": "December 28, 1856 \u2013 February 3, 1924",
        "IMG filepath": "../asset/img/28_Wilson.jpeg",
        "Description": "Wilson implemented significant domestic reforms, including the Federal Reserve Act and the Clayton Antitrust Act, while advocating for a vision of international cooperation. He led the nation during World War I, promoting the League of Nations as a means to ensure lasting peace. His idealism and focus on democracy shaped U.S. foreign policy for years to come."
    },
    "29": {
        "No": "29",
        "Name": " Warren G. Harding",
        "Term Years": "1921\u20131923",
        "Vice President": "Calvin Coolidge",
        "First Lady": "Florence Harding ",
        "Party": "Republican",
        "Birth-Death ": "November 2, 1865 \u2013 August 2, 1923",
        "IMG filepath": "../asset/img/29_Harding.jpeg",
        "Description": "Harding's presidency is often remembered for the call for a \"return to normalcy\" after WWI and for significant corruption scandals, including the Teapot Dome affair. He focused on economic recovery and reduced government intervention in business. His sudden death left many of his policies unfulfilled."
    },
    "30": {
        "No": "30",
        "Name": " Calvin Coolidge",
        "Term Years": "1923\u20131929",
        "Vice President": "Charles Curtis",
        "First Lady": "Grace Coolidge",
        "Party": "Republican",
        "Birth-Death ": "July 4, 1872 \u2013 January 5, 1933",
        "IMG filepath": "../asset/img/30_Coolidge.jpeg",
        "Description": "Coolidge promoted business and economic growth, advocating for low taxes and minimal government intervention. His presidency is associated with the economic prosperity of the Roaring Twenties, but he faced growing social tensions. He famously stated that \"the business of America is business,\" emphasizing a laissez-faire approach."
    },
    "31": {
        "No": "31",
        "Name": " Herbert Hoover",
        "Term Years": "1929\u20131933",
        "Vice President": "Charles Curtis",
        "First Lady": "Lou Hoover",
        "Party": "Republican",
        "Birth-Death ": "August 10, 1874 \u2013 October 20, 1964",
        "IMG filepath": "../asset/img/31_Hoover.jpeg",
        "Description": "Hoover's presidency was defined by the onset of the Great Depression, leading to widespread unemployment and economic hardship. He believed in limited government intervention, which led to criticism of his response to the crisis. His efforts to alleviate suffering were seen as inadequate, contributing to his electoral defeat."
    },
    "32": {
        "No": "32",
        "Name": " Franklin D. Roosevelt",
        "Term Years": "1933\u20131945",
        "Vice President": "John Nance Garner, Henry A. Wallace, Harry S. Truman",
        "First Lady": "Eleanor Roosevelt ",
        "Party": "Democratic",
        "Birth-Death ": "January 30, 1882 \u2013 April 12, 1945",
        "IMG filepath": "../asset/img/32_Roosevelt.jpeg",
        "Description": "FDR implemented the New Deal, a series of programs aimed at economic recovery during the Great Depression, emphasizing relief, recovery, and reform. He led the nation through World War II, positioning the U.S. as a global leader. His innovative approach to governance reshaped the role of the federal government."
    },
    "33": {
        "No": "33",
        "Name": " Harry S. Truman",
        "Term Years": "1945\u20131953",
        "Vice President": "Alben W. Barkley",
        "First Lady": "Elizabeth Truman",
        "Party": "Democratic",
        "Birth-Death ": "May 8, 1884 \u2013 December 26, 1972",
        "IMG filepath": "../asset/img/33_Truman.jpeg",
        "Description": "Truman oversaw the end of WWII and made the controversial decision to use atomic bombs on Japan. His presidency established the Truman Doctrine, aiming to contain communism and support free peoples. He faced challenges of post-war reconstruction and the onset of the Cold War."
    },
    "34": {
        "No": "34",
        "Name": " Dwight D. Eisenhower",
        "Term Years": "1953\u20131961",
        "Vice President": "Richard Nixon",
        "First Lady": "Mamie Eisenhower",
        "Party": "Republican",
        "Birth-Death ": "October 14, 1890 \u2013 March 28, 1969",
        "IMG filepath": "../asset/img/34_Eisenhower.jpeg",
        "Description": "Eisenhower focused on Cold War containment and promoted civil rights, while overseeing economic growth and the creation of the Interstate Highway System. He emphasized a balanced approach to foreign policy, navigating tensions with the Soviet Union. His presidency is marked by stability and prosperity."
    },
    "35": {
        "No": "35",
        "Name": " John F. Kennedy",
        "Term Years": "1961\u20131963",
        "Vice President": "Lyndon B. Johnson",
        "First Lady": "Jacqueline Kennedy",
        "Party": "Democratic",
        "Birth-Death ": "May 29, 1917 \u2013 November 22, 1963",
        "IMG filepath": "../asset/img/35_Kennedy.jpeg",
        "Description": "Kennedy's presidency was characterized by a focus on civil rights, space exploration, and the Cold War, notably during the Cuban Missile Crisis. His call for a \"New Frontier\" aimed at addressing social issues and promoting global peace. His assassination in 1963 shocked the nation and left a lasting impact."
    },
    "36": {
        "No": "36",
        "Name": " Lyndon B. Johnson",
        "Term Years": "1963\u20131969",
        "Vice President": "Hubert Humphrey",
        "First Lady": "Claudia Johnson",
        "Party": "Democratic",
        "Birth-Death ": "August 27, 1908 \u2013 January 22, 1973",
        "IMG filepath": "../asset/img/36_Johnson.jpeg",
        "Description": "Johnson expanded civil rights legislation and launched the Great Society programs, aimed at eliminating poverty and racial injustice. His presidency was also marked by escalating U.S. involvement in the Vietnam War, leading to widespread protests. His ambitious domestic agenda faced challenges amid growing dissent."
    },
    "37": {
        "No": "37",
        "Name": " Richard Nixon",
        "Term Years": "1969\u20131974",
        "Vice President": "Spiro Agnew, Gerald Ford",
        "First Lady": "Thelma Nixon",
        "Party": "Republican",
        "Birth-Death ": "January 9, 1913 \u2013 April 22, 1994",
        "IMG filepath": "../asset/img/37_Nixon.jpeg",
        "Description": "Nixon's presidency focused on foreign policy achievements, including opening relations with China and pursuing d\u00e9tente with the Soviet Union. He faced significant domestic challenges, including the Vietnam War and civil unrest. His presidency ended in scandal, culminating in his resignation over the Watergate scandal."
    },
    "38": {
        "No": "38",
        "Name": " Gerald Ford",
        "Term Years": "1974\u20131977",
        "Vice President": "Nelson Rockefeller",
        "First Lady": "Elizabeth Ford",
        "Party": "Republican",
        "Birth-Death ": "July 14, 1913 \u2013 December 26, 2006",
        "IMG filepath": "../asset/img/38_Ford.jpeg",
        "Description": "Ford took office following Nixon's resignation, focusing on healing the nation and restoring trust in government. He faced economic challenges, including inflation and recession, while dealing with the aftermath of the Vietnam War. His controversial decision to pardon Nixon was met with public backlash."
    },
    "39": {
        "No": "39",
        "Name": " Jimmy Carter",
        "Term Years": "1977\u20131981",
        "Vice President": "Walter Mondale",
        "First Lady": "Rosalynn Carter",
        "Party": "Democratic",
        "Birth-Death ": "October 1, 1924 \u2013 (living)",
        "IMG filepath": "../asset/img/39_Carter.jpeg",
        "Description": "Carter emphasized human rights and energy conservation, promoting a moral foreign policy. His presidency faced significant challenges, including the Iran hostage crisis and economic struggles. Despite his efforts at diplomacy and reform, he was often criticized for his handling of domestic issues."
    },
    "40": {
        "No": "40",
        "Name": " Ronald Reagan",
        "Term Years": "1981\u20131989",
        "Vice President": "George H. W. Bush",
        "First Lady": "Nancy Reagan ",
        "Party": "Republican",
        "Birth-Death ": "February 6, 1911 \u2013 June 5, 2004",
        "IMG filepath": "../asset/img/40_Reagan.jpeg",
        "Description": "Reagan championed conservative economic policies, tax cuts, and a strong military, promoting an \"America First\" agenda. His presidency is marked by a reduction in government regulation and a focus on defeating communism, particularly in Latin America. He played a key role in ending the Cold War through diplomatic negotiations."
    },
    "41": {
        "No": "41",
        "Name": " George H. W. Bush",
        "Term Years": "1989\u20131993",
        "Vice President": "Dan Quayle",
        "First Lady": "Barbara Bush",
        "Party": "Republican",
        "Birth-Death ": "June 12, 1924 \u2013 November 30, 2018",
        "IMG filepath": "../asset/img/41_Bush.jpeg",
        "Description": "Bush's presidency focused on foreign policy successes, including the Gulf War and the fall of the Berlin Wall, which marked the end of the Cold War. Domestically, he faced economic challenges, including a recession. His commitment to a \"kinder, gentler\" nation defined his approach to governance."
    },
    "42": {
        "No": "42",
        "Name": " Bill Clinton",
        "Term Years": "1993\u20132001",
        "Vice President": "Al Gore",
        "First Lady": "Hillary Clinton",
        "Party": "Democratic",
        "Birth-Death ": "August 19, 1946",
        "IMG filepath": "../asset/img/42_Clinton.jpeg",
        "Description": "Clinton's presidency is marked by economic prosperity, the implementation of welfare reform, and the North American Free Trade Agreement (NAFTA). He faced significant political challenges, including impeachment over personal conduct, but was acquitted by the Senate. His focus on centrist policies helped reshape the Democratic Party."
    },
    "43": {
        "No": "43",
        "Name": " George W. Bush",
        "Term Years": "2001\u20132009",
        "Vice President": "Dick Cheney",
        "First Lady": "Laura Bush",
        "Party": "Republican",
        "Birth-Death ": "July 6, 1946",
        "IMG filepath": "../asset/img/43_Bush.jpeg",
        "Description": "Bush's presidency was defined by the response to the 9/11 attacks, leading to military action in Afghanistan and Iraq. His administration implemented significant tax cuts and emphasized national security, but also faced criticism for its handling of the economy. The financial crisis in 2008 marked the end of his presidency."
    },
    "44": {
        "No": "44",
        "Name": " Barack Obama",
        "Term Years": "2009\u20132017",
        "Vice President": "Joe Biden",
        "First Lady": "Michelle Obama",
        "Party": "Democratic",
        "Birth-Death ": "August 4, 1961",
        "IMG filepath": "../asset/img/44_Obama.jpeg",
        "Description": "Obama focused on recovering from the Great Recession, implementing the Affordable Care Act and emphasizing climate change initiatives. He aimed to improve foreign relations, notably through the Iran nuclear deal and the Paris Agreement. His presidency was marked by significant social change and ongoing partisan divisions."
    },
    "45": {
        "No": "45",
        "Name": " Donald Trump",
        "Term Years": "2017\u20132021",
        "Vice President": "Mike Pence",
        "First Lady": "Melania Trump",
        "Party": "Republican",
        "Birth-Death ": "June 14, 1946",
        "IMG filepath": "../asset/img/45_Trump.jpeg",
        "Description": "Trump's presidency emphasized \"America First\" policies, including immigration reform and trade tariffs, and he appointed three Supreme Court justices. His administration faced significant controversy and division, culminating in two impeachments\u2014both resulting in acquittals. His impact on American politics remains a subject of intense debate."
    },
    "46": {
        "No": "46",
        "Name": " Joe Biden",
        "Term Years": "2021\u2013present",
        "Vice President": "Kamala Harris",
        "First Lady": "Jill Biden",
        "Party": "Democratic",
        "Birth-Death ": "November 20, 1942",
        "IMG filepath": "../asset/img/46_Biden.jpeg",
        "Description": "Biden's presidency has focused on uniting the nation post-COVID-19 pandemic, implementing economic stimulus measures, and addressing climate change. He has emphasized social justice, infrastructure development, and rebuilding alliances abroad. His administration faces ongoing challenges, including political polarization and economic recovery efforts."
    }
}

    return jsonify(presidents)