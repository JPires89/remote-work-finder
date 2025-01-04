import streamlit as st

# Configurações iniciais do app
st.set_page_config(page_title="Remote Work Finder", layout="centered", initial_sidebar_state="collapsed")

# Gerenciar o estado inicial da página
if "page" not in st.session_state:
    st.session_state["page"] = "Home"


def main():
    # Layout da página inicial
    st.title("🌍 Remote Work Finder")
    st.markdown("### Discover platforms for remote jobs worldwide!")

    st.markdown(
        """
        Welcome to **Remote Work Finder**! Find the best platforms for remote work opportunities, organized by categories.
        """
    )

    # Layout principal
    if st.session_state["page"] == "Home":
        show_home()
    else:
        show_category(st.session_state["page"])


# Página inicial

def show_home():
    st.header("Featured Categories")

    categories = [
        ("Freelance", "🖥"),
        ("Microjobs", "⚙️"),
        ("Translation", "🌐"),
        ("Consulting", "📊"),
        ("Technical Support", "🔧")
    ]

    for category, icon in categories:
        with st.container():
            st.markdown(f"{icon} **{category}**")
            if st.button(f"Explore {category}", key=category):
                st.session_state["page"] = category


# Página de categoria específica
def show_category(category_name):
    platforms = {
        "Freelance": [
            {"name": "Upwork", "description": "A global platform for freelance projects.",
             "link": "https://www.upwork.com", "earnings": "$50-$200/day"},
            {"name": "Freelancer", "description": "Find freelance jobs in various industries.",
             "link": "https://www.freelancer.com", "earnings": "$40-$150/day"},
            {"name": "Toptal", "description": "Exclusive network of top freelancers.", "link": "https://www.toptal.com",
             "earnings": "$100-$300/day"},
            {"name": "Guru", "description": "Freelance jobs for professionals.", "link": "https://www.guru.com",
             "earnings": "$30-$120/day"},
            {"name": "PeoplePerHour", "description": "Freelance jobs for various skills.",
             "link": "https://www.peopleperhour.com", "earnings": "$20-$100/day"}
        ],
        "Microjobs": [
            {"name": "Amazon MTurk", "description": "Complete microtasks for businesses.",
             "link": "https://www.mturk.com", "earnings": "$10-$50/day"},
            {"name": "Clickworker", "description": "Earn money with small online tasks.",
             "link": "https://www.clickworker.com", "earnings": "$15-$70/day"},
            {"name": "Microworkers", "description": "Short tasks for small earnings.",
             "link": "https://www.microworkers.com", "earnings": "$10-$40/day"},
            {"name": "Fiverr", "description": "Offer quick services starting at 5 USD.", "link": "https://www.fiverr.com",
             "earnings": "$20-$100/day"},
            {"name": "RapidWorkers", "description": "Quick tasks for extra income.",
             "link": "https://www.rapidworkers.com", "earnings": "$5-$30/day"}
        ],
        "Translation": [
            {"name": "Gengo", "description": "Earn money translating texts.", "link": "https://www.gengo.com",
             "earnings": "$25-$100/day"},
            {"name": "ProZ", "description": "Join a network of professional translators.",
             "link": "https://www.proz.com", "earnings": "$30-$150/day"},
            {"name": "Smartcat", "description": "Collaborate with translation teams.",
             "link": "https://www.smartcat.com", "earnings": "$20-$90/day"},
            {"name": "TranslatorsCafe", "description": "Find translation jobs globally.",
             "link": "https://www.translatorscafe.com", "earnings": "$25-$80/day"},
            {"name": "OneHourTranslation", "description": "Fast translation services.",
             "link": "https://www.onehourtranslation.com", "earnings": "$20-$100/day"}
        ],
        "Consulting": [
            {"name": "Clarity.fm", "description": "Provide expert advice on demand.", "link": "https://www.clarity.fm",
             "earnings": "$50-$300/day"},
            {"name": "Toptal", "description": "Consulting for top-tier freelancers.", "link": "https://www.toptal.com",
             "earnings": "$100-$400/day"},
            {"name": "Catalant", "description": "On-demand business consulting.", "link": "https://www.gocatalant.com",
             "earnings": "$80-$250/day"},
            {"name": "HourlyNerd", "description": "Business consulting platform.", "link": "https://www.hourlynerd.com",
             "earnings": "$70-$200/day"},
            {"name": "GLG", "description": "Expert network for consulting jobs.", "link": "https://www.glginsights.com",
             "earnings": "$150-$500/day"}
        ],
        "Technical Support": [
            {"name": "Support.com", "description": "Offer remote tech support services.",
             "link": "https://www.support.com", "earnings": "$30-$100/day"},
            {"name": "LivePerson", "description": "Provide customer support for businesses.",
             "link": "https://www.liveperson.com", "earnings": "$50-$200/day"},
            {"name": "OutPLEX", "description": "Customer and tech support services.", "link": "https://www.outplex.com",
             "earnings": "$40-$150/day"},
            {"name": "Working Solutions", "description": "Virtual tech support jobs.",
             "link": "https://www.workingsolutions.com", "earnings": "$50-$180/day"},
            {"name": "HelpFlow", "description": "E-commerce live chat support.", "link": "https://www.helpflow.net",
             "earnings": "$30-$120/day"}
        ]
    }

    st.header(f"{category_name} Platforms")
    for platform in platforms[category_name]:
        with st.container():
            st.markdown(
                f"**{platform['name']}**: {platform['description']} [Visit Site]({platform['link']}) - *Earnings: {platform['earnings']}*")

    if st.button("Back to Home"):
        st.session_state["page"] = "Home"


# Página sobre
def show_about():
    st.header("About Remote Work Finder")
    st.markdown(
        """
        Remote Work Finder is designed to help individuals explore remote work opportunities globally. 
        Our platform provides an easy-to-use interface for discovering jobs and connecting with platforms.
        """
    )


# Executar o app
if __name__ == "__main__":
    main()
