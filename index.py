from healper_func import lander_pg
from scrappers import world_gnews


def create_pg():
   
    from scrappers import headlines_gnews, world_gnews,health_gnews,tech,business_gnews
    from healper_func import lander_pg,index_create
    page_details=[
        ["Indian Headlines",
        """INDIA, OUR COUNTRY IS A HUGE AND BEAUTIFUL LAND FULL OF WONDERS.<br>
    FROM THE HIMALAYAS TO THE INDIAN OCEAN, THE DESERT OF THAR IN THE SNOWY MOUNTAINS OF SIKKIM, IT IS A COUNTRY FULL OF BEAUTIFUL LANDSCAPES AND BEAUTIFUL PEOPLE. INDIA IS A UNIQUE COUNTRY WITH DIVERSITY.<br>
    "UNITY IS DIVERSITY" IS THE MAIN SLOGAN OF THE COUNTRY""",
    "docs/images/banners/india.jpg",
    headlines_gnews(),
    'india.html'],
    ["World",
    "THE WORLD, VIEWED PHILOSOPHICALLY, REMAINS A SERIES OF SLAVE CAMPS, WHERE CITIZENS � TAX LIVESTOCK � LABOR UNDER THE CHAINS OF ILLUSION IN THE SERVICE OF THEIR MASTERS.",
    "docs/images/banners/world.jpg",
    world_gnews(),
    'world.html'],
    ['Business',
    'ALBERT EINSTEIN ONCE SAID �COMPOUND INTEREST IS THE EIGHTH WONDER OF THE WORLD.',
    'docs/images/banners/business.jpeg',
    business_gnews(),
    'business.html'],
    ['Techies',
    "IT'S NOT A FAITH IN TECHNOLOGY. IT'S FAITH IN PEOPLE.",
    "docs/images/banners/tech.jpg",
    tech(),
    'tech.html'],
    ["Health",
    "GIVE A MAN HEALTH AND A COURSE TO STEER, AND HE�LL NEVER STOP TO TROUBLE ABOUT WHETHER HE�S HAPPY OR NOT.",
    "docs/images/banners/med.jpg",
    health_gnews(),
    "health.html"]]
    index_create()
    for i in page_details:
        lander_pg(title=i[0],
        tagline=i[1],
        title_img=i[2],
        article_lst=i[3],
        filename=i[4])

create_pg()









