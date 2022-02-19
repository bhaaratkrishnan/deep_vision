def article_object(url):
    from newspaper import Article
    article=Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article
def lander_pg(title,tagline,title_img,article_lst,filename):
    land_1=f"""<!DOCTYPE HTML>
    <html>
        <head>
            <title>{title}</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
            <link rel="stylesheet" href="assets/css/main.css" />
            <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
        </head>
        <body class="is-preload"><!-- Wrapper -->
                <div id="wrapper">

                    <!-- Header -->
                    <!-- Note: The "styleN" class below should match that of the banner element. -->
                        <header id="header" class="alt style2">
                            <a href="index.html" class="logo"><strong>Deep Vision</strong> <span>by BlueMorning</span></a>
                            </header>
                            <!-- Banner -->
                    <!-- Note: The "styleN" class below should match that of the header element. -->
                        <section id="banner" class="style2">
                            <div class="inner">
                                <span class="image">
                                    <img src={title_img} alt="" />
                                </span>
                                <header class="major">
                                    <h1>{title}</h1>
                                </header>
                                <div class="content">
                                    <p>{tagline}</p>
                                </div>
                            </div>
                        </section><div id="main"><section id="two" class="spotlights">"""
    land_2=""
    for j in article_lst:
        i=article_object(j)
        land_2_sec=f"""<section><a href={i.url} class="image">

                                            <img src={i.top_image} height="515"
                                            width="576" alt data-position="center center"/>
                                        </a>
                                        <div class="content">
                                            <div class="inner">
                                                <header class="major">
                                                    <h3>{i.title}</h3>
                                                </header>
                                                <p>{i.summary}</p>
                                                <ul class="actions">
                                                    <li><a href={i.url} class="button">Learn more</a></li>
                                                </ul>
                                            </div>
                                        </div>
                                    </section>"""
        land_2+=land_2_sec
    land_3="""</div>

                    
                    </div>

            <!-- Scripts -->
                <script src="assets/js/jquery.min.js"></script>
                <script src="assets/js/jquery.scrolly.min.js"></script>
                <script src="assets/js/jquery.scrollex.min.js"></script>
                <script src="assets/js/browser.min.js"></script>
                <script src="assets/js/breakpoints.min.js"></script>
                <script src="assets/js/util.js"></script>
                <script src="assets/js/main.js"></script>

        </body>
    </html>"""
    with open('docs/'+filename,'w',encoding="utf8") as file:
        file.write(land_1+land_2+land_3)

def index_create():
    from datetime import date
    today=date.today().strftime('%b %d %Y')

    index=f"""<!DOCTYPE HTML>


        <html>
            <head>
                <title>Deep Vision</title>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
                <link rel="stylesheet" href="assets/css/main.css" />
                <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
            </head>
            <body class="is-preload">

                <!-- Wrapper -->
                    <div id="wrapper">

                        <!-- Header -->
                            <header id="header" class="alt">
                                <a href="index.html" class="logo"><strong>Deep Vision</strong> <span>by BlueMorning</span></a>
                                
                            </header><section id="banner" class="major">
                                <div class="inner">
                                    <header class="major">
                                        <h1>Hi, I am Deep Vision...</h1>
                                    </header>
                                    <div class="content">
                                        <p> Walk with time while reading big lines <br />
                                        {today}</p>
                                        <ul class="actions">
                                            <li><a href="#one" class="button next scrolly">Get Started</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </section>
        
                        <!-- Main -->
                            <div id="main">

                                <!-- One -->
                                    <section id="one" class="tiles">
                                        <article>
                                            <span class="image">
                                                <img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/e0811a38119199.5756869054322.png" alt="" />
                                            </span>
                                            <header class="major">
                                                <h3><a href="latest.html" class="link">Lastest News</a></h3>
                                                <p>It’s a New Story Here!</p>
                                            </header>
                                        </article>
                                        <article>
                                            <span class="image">
                                                <img src="https://www.teahub.io/photos/full/46-468099_india-flag-hd-background-wallpaper-yosemite-national-park.jpg" alt="" />
                                            </span>
                                            <header class="major">
                                                <h3><a href="india.html" class="link">Indian Headlines</a></h3>
                                                <p>Nothing but authentic</p>
                                            </header>
                                        </article>
                                        <article>
                                            <span class="image">
                                                <img src="https://wallpaperaccess.com/full/199469.jpg" alt="" />
                                            </span>
                                            <header class="major">
                                                <h3><a href="world.html" class="link">World</a></h3>
                                                <p>The World in a headline</p>
                                            </header>
                                        </article>
                                        <article>
                                            <span class="image">
                                                <img src="https://wallpaperaccess.com/full/656665.jpg" alt="" />
                                            </span>
                                            <header class="major">
                                                <h3><a href="business.html" class="link">Business</a></h3>
                                                <p>Hey Economy, How you doing!</p>
                                            </header>
                                        </article>
                                        <article>
                                            <span class="image">
                                                <img src="https://cdn.wallpapersafari.com/79/46/pDyIbY.jpg" alt="" />
                                            </span>
                                            <header class="major">
                                                <h3><a href="tech.html" class="link">Techie</a></h3>
                                                <p>Andd I forgot to charge my car :(</p>
                                            </header>
                                        </article>
                                        <article>
                                            <span class="image">
                                                <img src="https://wallpaperaccess.com/full/4310878.jpg" alt="" />
                                            </span>
                                            <header class="major">
                                                <h3><a href="health.html" class="link">Health</a></h3>
                                                <p>Simply Health and Science</p>
                                            </header>
                                        </article>
                                    </section><!-- Two -->
                                    <section id="two">
                                        <div class="inner">
                                            <header class="major">
                                                <h2>Word of the Day : Hew</h2>
                                            </header>
                                            <p>Make Or Shape As With An Axe<br>
                                            Strike With An Axe; Cut Down, Strike<br></p>
                                            <ul class="actions">
                                                <li><a href="lastest.html" class="button next">Get Started</a></li>
                                            </ul>
                                        </div></section></div></div><!-- Scripts -->
                    <script src="assets/js/jquery.min.js"></script>
                    <script src="assets/js/jquery.scrolly.min.js"></script>
                    <script src="assets/js/jquery.scrollex.min.js"></script>
                    <script src="assets/js/browser.min.js"></script>
                    <script src="assets/js/breakpoints.min.js"></script>
                    <script src="assets/js/util.js"></script>
                    <script src="assets/js/main.js"></script>

            </body>
        </html>
    """
    with open('docs/index.html','w') as file:
        file.write(index)
        print('Index written Sucessfully!')






