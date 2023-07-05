from flask import Flask, render_template

app = Flask(__name__, template_folder="public", static_folder="src")


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/contact-us")
def contact_us():
    return render_template("pages/contact-us.html")


@app.route("/about-us")
def about_us():
    return render_template("pages/about-us.html")


@app.route("/faqs")
def faqs():
    return render_template("pages/faqs.html")


@app.route("/team")
def team():
    return render_template("pages/team.html")


@app.route("/privacy-policy")
def privacy_policy():
    return render_template("pages/privacy-policy.html")


@app.route("/terms-and-conditions")
def terms_and_conditions():
    return render_template("pages/terms-and-conditions.html")


@app.route("/terms-and-conditions")
def cookies_policy():
    return render_template("pages/cookies-policy.html")


@app.route("/blogs")
def blogs():
    return render_template("pages/blogs.html")


@app.route("/blog-details")
def blog_details():
    return render_template("pages/blog-details.html")


@app.route("/projects")
def projects():
    return render_template("pages/projects.html")


@app.route("/product-details")
def project_detais():
    return render_template("pages/product-details.html")


@app.route("/services")
def services():
    return render_template("pages/services.html")


@app.route("/service/branding")
def service_branding():
    return render_template("pages/service-branding.html")


@app.route("/service/ui-ux")
def service_graphics_design():
    return render_template("pages/service-graphics-design.html")


@app.route("/service/web-development")
def service_web_development():
    return render_template("pages/service-web-development.html")


@app.route("/service/mobile-app-development")
def service_app_development():
    return render_template("pages/service-app-development.html")


@app.route("/service/digital-marketing")
def service_digital_marketing():
    return render_template("pages/service-digital-marketing.html")


@app.route("/service/cyber-security")
def service_cyber_security():
    return render_template("pages/service-cyber-security.html")


@app.route("/service/devops")
def service_devops():
    return render_template("pages/service-devops.html")


@app.route("/service/networking")
def service_networking():
    return render_template("pages/service-networking.html")


@app.route("/service/erp-development")
def service_erp_development():
    return render_template("pages/service-erp-development.html")


@app.route("/service/database-administration")
def service_database_admininstration():
    return render_template("pages/service-database-administration.html")


@app.route("/service/server-administration")
def service_server_administration():
    return render_template("pages/service-server-administration.html")


@app.route("/service/cloud-management")
def service_cloud_management():
    return render_template("pages/service-cloud-management.html")


@app.route("/service/manage-hosting")
def service_manage_hosting():
    return render_template("pages/service-manage-hosting.html")


@app.route("/service/technical-support")
def service_technical_support():
    return render_template("pages/service-technical-support.html")


@app.route("/service/business-analysis")
def service_business_analysis():
    return render_template("pages/service-business-analysis.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("pages/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    # note that we set the 500 status explicitly
    return render_template("pages/500.html"), 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)
