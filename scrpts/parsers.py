__author__ = 'kuroi'


def date_transform(date, sep='-', date_format='to_sql'):
    """The function transforms date formats from
    dd.mm.yyyy to yyyy-mm-dd by default key date_format='to_sql'
    and vice versa in ANY other case. Returns transformed date-string.
    """
    if date_format == 'to_sql':
        day = date[:2]
        month = date[3:5]
        year = date[-4:]
        return year + sep + month + sep + day
    else:
        day = date[-2:]
        month = date[5:7]
        year = date[0:4]
        return day + sep + month + sep + year


def flag_check(db_file='./dbs/cn.db'):
    from sqlite3 import connect
    db_connect = connect(db_file)
    ids = db_connect.execute('''SELECT CUSTOMER_ID FROM NAMES''')
    for cid in ids:
        by_id = db_connect.execute('''SELECT ID, P_DATE, C_DATE FROM NOTIFY 
                                    WHERE CUSTOMER_ID == ? ORDER BY ID ASC''', cid).fetchall()
        for row in range(1, len(by_id)):
            p_row = row - 1
            if (by_id[row][1] > by_id[p_row][1]) and (by_id[row][1] < by_id[p_row][2]):
                db_connect.execute('''UPDATE NOTIFY SET B_B = 'Да' WHERE ID == ?''', (by_id[p_row][0],))
            elif by_id[row][1] > by_id[p_row][2]:
                db_connect.execute('''UPDATE NOTIFY SET B_A = 'Да' WHERE ID == ?''', (by_id[p_row][0],))
    db_connect.commit()
    db_connect.close()


def import_from_txt(db_file='./dbs/cn.db', input_path='./input/', prefix='NTS-'):
    """This function provides parsing and importing data from text tables provided by 1C into SQLite database.
    Typical string from 1C tables is:
    Реализация товаров и услуг NTS-0000000 от 01.01.2001 00:00:00\tCustomer's name, 89000000000\t01.02.2001\t1\n
    """
    import os
    import sqlite3
    from shutil import copyfile

    # try:
    copyfile(db_file, './dbs/baka')                     # copying our db before merging with input. safety first
    # except IOError:                                   # uncomment in case of ridiculous error.
    #     print('back-up error.')                       # TODO: if there is any chance, use means of SQLite for backup.
    #     return 12

    sub_0 = 'Параметры'                                 # just some magic strings.

    imported_files = [f for f in os.listdir(input_path) if f[-4:] == '.txt']    # a list of files on import.

    if not imported_files:                              # if the list is empty
        print('no files to parse')                      # nothing special, just nothing to import.
        return

    for file in imported_files:                         # listing all files in the given directory
        file = os.path.join(input_path, file)
        txt_read = open(file, 'r', encoding='UTF8').readlines()     # opening the text file with table by strings

        if sub_0 not in txt_read[1]:
            continue                                    # if there is no line with sub_0 -- continue to the next file

        while prefix not in txt_read[0]:                # if there are garbage lines in the beginning of file
            txt_read.pop(0)                             # just pop them out

        with open(file, 'w', encoding='UTF8') as txt_write:              # now we need to write changes
            txt_write.writelines(txt_read)              # so that future listing knew we already used this table.

        db_connect = sqlite3.connect(db_file)           # connecting to the db.
        db_connect.execute('PRAGMA foreign_keys = ON')
        for line in txt_read:                           # parsing every single line in table
            # (ID) (NAME) (PHONE) (P_DATE) (C_DATE) CONTRACT (CUSTOMERS_ID)
            PHONE = line[line.find('\t', 22) + 1:line.find('\t', 22) + 12]
            te = PHONE[0:2]
            if PHONE[0:2] != '89':
                continue
            CUSTOMER_ID = line[12:21]                  # customer's id from 1c for NAMES table
            NAME = line[line.find('\t', 20) + 1:line.find('\t', 22)]           # customers' name

            # writing new customer to the NAMES table:
            db_connect.execute('''INSERT OR IGNORE INTO NAMES (CUSTOMER_ID, NAME, PHONE, COMMENT, AGREED)
                                VALUES (?, ?, ?, "", 'Да')''', (CUSTOMER_ID, NAME, PHONE))

            ID = line[4:11]                             # that's the purchase id. and it's key for the SQLite table
            line = line[line.find('\t', 22) + 13:]      # cutting line down for known variables
            P_DATE = date_transform(line[:10])          # date of purchase
            last_tab = line.rfind('\t')
            C_DATE = date_transform(line[last_tab - 10:last_tab])   # planned date of next purchase
            if line[-2] != '\t':
                CONTRACT = 'Да'
            else:
                CONTRACT = 'Нет'

            # writing new purchase to the NOTIFY table
            db_connect.execute('''INSERT OR IGNORE INTO
            NOTIFY (ID, CUSTOMER_ID, P_DATE, C_DATE, INFORMED, CONTRACT, B_B, B_A)
            VALUES (?, ?, ?, ?, 'Нет', ?, 'Нет', 'Нет')''', (ID, CUSTOMER_ID, P_DATE, C_DATE, CONTRACT))
        db_connect.commit()
        db_connect.close()
    flag_check(db_file)

    # TODO: move used text files to './input/used/'
