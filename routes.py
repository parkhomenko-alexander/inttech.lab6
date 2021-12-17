from app import app
from app import container


@app.route('/health', methods=['GET', 'POST'])
def get_helth():
    return {'env': (container.service().get_env())}

@app.route('/', methods=['GET', 'POST'])
def inx():
    return 'hello'
