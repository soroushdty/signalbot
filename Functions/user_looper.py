def userlooper(userlist):
    for userobject in userlist:
        threading.Thread(target=outer_wrapper, args=(userobject))
        logging.info(f'Outer thread started for user{userobject.userid}')