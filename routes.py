from app import app
from app import container


@app.route('/helth', methods=['GET', 'POST'])
def get_helth():
    return {'env': (container.service().get_env())}
