from fastapi.encoders import jsonable_encoder


def encode_input(data) -> dict:
    '''
    This function convert an object to json format removing None type fields.
    '''
    data = jsonable_encoder(data)
    data = {k: v for k, v in data.items() if v is not None}
    return data