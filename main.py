from flask import Flask, render_template
from flask_frozen import Freezer
from utils import if_file_exist

app = Flask(__name__, template_folder="public", static_folder="assets")

# Route - Page - Function
routes = [
    {"page": "test", "url": "test"},
    {"page": "index", "url": ""},
    {"page": "about-us", "url": "about-us"},
    {"page": "contact-us", "url": "contact-us"},
    {"page": "team", "url": "team"},
    {"page": "team-details", "url": "team-details"},
    {"page": "faqs", "url": "faqs"},
    {"page": "terms-and-conditions", "url": "terms-and-conditions"},
    {"page": "privacy-policy", "url": "privacy-policy"},
    {"page": "cookies-policy", "url": "cookies-policy"},
    {"page": "blogs", "url": "blogs"},
    {"page": "blog-details", "url": "blog-details"},
    {"page": "news", "url": "news"},
    {"page": "news-details", "url": "news-details"},
    {"page": "careers", "url": "careers"},
    {"page": "job-details", "url": "job-details"},
    {"page": "projects", "url": "projects"},
    {"page": "project-details", "url": "project-details"},
    {"page": "products", "url": "products"},
    {"page": "product-details", "url": "product-details"},
    {"page": "services", "url": "services"},
    {"page": "service-mobile-app-development", "url": "service-mobile-app-development"},
    {"page": "service-web-development", "url": "service-web-development"},
    {"page": "service-erp-development", "url": "service-erp-development"},
    {"page": "service-branding", "url": "service-branding"},
    {"page": "service-digital-marketing", "url": "service-digital-marketing"},
    {
        "page": "service-database-administration",
        "url": "service-database-administration",
    },
    {"page": "service-server-administration", "url": "service-server-administration"},
    {"page": "service-cyber-security", "url": "service-cyber-security"},
    {"page": "service-networking", "url": "service-networking"},
    {"page": "service-managed-hosting", "url": "service-managed-hosting"},
    {"page": "service-cloud-hosting", "url": "service-cloud-hosting"},
    {"page": "service-technical-support", "url": "service-technical-support"},
    {"page": "service-business-analysis", "url": "service-business-analysis"},
    {"page": "service-devops", "url": "service-devops"},
    {"page": "service-seo", "url": "service-seo"},
    {"page": "service-graphics-designing", "url": "service-graphics-designing"},
]

for route in routes:
    if if_file_exist(route["page"]):
        function = f"""
@app.route('/{route["url"]}')
def {route["page"].replace("-","_")}():
    return render_template('pages/{route["page"]}.html')
"""
        exec(function)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("pages/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    # note that we set the 500 status explicitly
    return render_template("pages/500.html"), 500


if __name__ == "__main__":
    # app.config["FREEZER_DESTINATION"] = "docs"  # Output folder for frozen files
    # freezer = Freezer(app)
    # freezer.freeze()  # Generate static files

    app.run(debug=True, port=8080)
