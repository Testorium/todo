from time import time

import jwt
from shared.settings import jwt_config


def generate_token(user_id: int):
    exp = time() + jwt_config.token_time

    payload = {
        "alg": jwt_config.algorithm,
        "sub": str(user_id),
        "exp": exp,
    }

    return jwt.encode(payload, jwt_config.secret_key, algorithm=jwt_config.algorithm)
