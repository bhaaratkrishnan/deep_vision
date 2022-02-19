def latest_running():
    from healper_func import article_object
    from scrappers import latest
    import time
    def latest_create(news_list):
        title='Latest News & Updates'
        title_img='docs/images/banners/latest.jpg'
        pg_1=f"""<!DOCTYPE HTML>
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
                                        <p></p>
                                    </div>
                                </div>
                            </section><div id="main">"""
        pg_2=""
        for i in news_list:
            i=article_object(i)
            summary=i.summary.split(".")
            summary="".join(summary[:2])
            pg_sec=f"""<section id="one">
                                        <div class="inner">
                                            <header class="major">
                                                <h2><a href={i.url}>{i.title}</a></h2>
                                            </header>
                                            <p>{i.summary}</p>
                                        </div>
                                    </section>"""
            pg_2+=pg_sec
        pg_3="""</div>

                        
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
        print("pages updated")
        with open("docs/latest.html","w",encoding='utf8') as file:
            file.write(pg_1+pg_2+pg_3)
    lst=[]
    while True:
        print("Checking")
        news=latest()
        if news not in lst:
            lst.append(news)
            #send reversed list
            latest_create(lst[::-1])
        time.sleep(100)
        if len(lst)>5:
            break
latest_running()