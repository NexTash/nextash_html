from flask import Flask, render_template
from flask_frozen import Freezer
from utils import if_file_exist

app = Flask(__name__, template_folder="public", static_folder="src")

routes = [
    "/:index:index",
    "/contact-us:contact_us:contact-us",
    "/about-us:about_us:about-us",
    "/faqs:faqs:faqs",
    "/team:team:expert-team",
    "/privacy-policy:privacy_policy:privacy-policy",
    "/terms-and-conditions:terms_and_conditions:terms-and-conditions",
    "/cookies-policy:cookies_policy:cookies-policy",
    "/blogs:blogs:blogs",
    "/blog-details:blog_details:blog-details",
    "/news:news:news",
    "/news-details:news_details:news-details",
    "/jobs:jobs:jobs",
    "/job-details:job_details:job-details",
    "/projects:projects:projects",
    "/product-details:project_detais:product-details",
    "/services:services:services",
    "/service/branding:service_branding:service-branding",
    "/service/ui-ux:service_graphics_design:service-ui-ux",
    "/service/web-development:service_web_development:service-web-development",
    "/service/mobile-app-development:service_app_development:service-mobile-app-development",
    "/service/digital-marketing:service_digital_marketing:service-digital-marketing",
    "/service/cyber-security:service_cyber_security:service-cyber-security",
    "/service/devops:service_devops:service-devops",
    "/service/networking:service_networking:service-networking",
    "/service/erp-development:service_erp_development:service-erp-development",
    "/service/database-administration:service_database_admininstration:service-database-administration",
    "/service/server-administration:service_server_administration:service-server-administration",
    "/service/cloud-management:service_cloud_management:service-cloud-management",
    "/service/manage-hosting:service_manage_hosting:service-manage-hosting",
    "/service/technical-support:service_technical_support:service-technical-support",
    "/service/business-analysis:service_business_analysis:service-business-analysis"
]

for row in routes:
    route, func_name, url = row.split(":")
    if if_file_exist(url):
            exec(f"""
@app.route('{route}')
def {func_name}():
    return render_template('pages/{url}.html')
"""
        )

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("pages/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    # note that we set the 500 status explicitly
    return render_template("pages/500.html"), 500

if __name__ == "__main__":
    app.config['FREEZER_DESTINATION'] = 'docs'  # Output folder for frozen files
    freezer = Freezer(app)
    freezer.freeze()  # Generate static files
    
    app.run(debug=True, port=8080)
