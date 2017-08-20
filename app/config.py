DEBUG = True

TEMPLATE_FOLDER = "../client/{folder}/".format(folder = "dev" if DEBUG else "prod")

STATIC_FOLDER = "../client/static/"
