from matplotlib import pyplot as plt

def getTXT(logtxt):
    """Clean the .txt file

    :param logtxt: Name of .txt file
    :type logtxt: str
    :return: *Unprocessed* messages
    :rtype: List
    :Example:
        .. code-block:: python

            getTXT('./tinder_log.txt')

        *will return a list of unprocessed messages*
    """
    log = open(logtxt, 'r', encoding='UTF-8').read()
    log = log.split('<div class="msgWrp')
    msg = ''
    for i in range(1, len(log)):
        msg = msg + str(log[i]) + '\n'
    return msg.split('\n')

def whoTHIS(msg):
    """To know who sent the message. 'Self' for yourself, 'Human' for the other *human*.

    :param msg: unprocessed message
    :type msg: str
    :return: Who sent this message
    :rtype: str
    :Example:
        .. code-block:: python

            whoTHIS(x)

        *x is an unprocessed message*
    """
    if 'Pos(r) Ta(start)' in msg:
        return 'Human'
    if 'Pos(r) Ta(end)' in msg:
        return 'Self'

def extractMSG(msg):
    """To extract the message sent in an unprocessed message.

    :param msg: unprocessed message
    :type msg: str
    :return: Processed message
    :rtype: str
    :Example:
        .. code-block:: python

            extractMSG(x)

        *x is an unprocessed message*
    """
    try:
        return msg.split('"text D(ib) Va(t)">')[1].split('</span></div></div>')[0]
    except:
        try:
            return msg.split('Mb(-10px)--ml">')[1].split('</span></div></div>')[0]
        except:
            return ''

def leng(msg):
    """To know the length of a message

    :param msg: processed message
    :type msg: str
    :return: length of message
    :rtype: int
    :Example:
        .. code-block:: python

            leng(x)

        *x is a processed message*
    """
    return len(msg)

def word(msg):
    """To know the number of words in a message

    :param msg: processed message
    :type msg: str
    :return: Number of words in message
    :rtype: int
    :Example:
        .. code-block:: python

            word(x)

        *x is a processed message*
    """
    msg = msg.replace(' ?', '').replace(' !', '').replace(' .', '').replace('?', '').replace('!', '').replace('.', '')
    return len(msg.split(' '))

def qm(msg):
    """To know if the message is a question

    :param msg: processed message
    :type msg: str
    :return: *1* if message is a question, *0* if not
    :rtype: int
    :Example:
        .. code-block:: python

            qm(x)

        *x is a processed message*
    """
    if '?' in msg:
        return 1
    else:
        return 0

def demo():
    """This is a demo to show stats about the conversation in a graph. Use it by changing to YOUR logs.

    :return: pyplot object
    :Example:
        .. code-block:: python

            demo().show()

        *will show the graph.*
    """
    A = getTXT('tinder.txt') # <--- Your .txt file
    q, ql, qw, qqm, h, hl, hw, hqm = 0,0,0,0,0,0,0,0

    for i in range(0, len(A)):
        if whoTHIS(A[i]) == 'Self':
            q+=1
            ql = ql + leng(extractMSG(A[i]))
            qw = qw + word(extractMSG(A[i]))
            if qm(extractMSG(A[i])) == 1:
                qqm+=1
            else:
                pass
        else:
            h += 1
            hl = hl + leng(extractMSG(A[i]))
            hw = hw + word(extractMSG(A[i]))
            if qm(extractMSG(A[i])) == 1:
                hqm += 1
            else:
                pass

    plt.xticks(rotation=50, fontsize=14)
    plt.grid(axis='y')
    plt.bar('% msg.\nTot. : '+str(q+h), round(q*100/(q+h), 2),color='blue', label='Self')
    plt.bar('% msg.\nTot. : '+str(q+h), round(h*100/(q+h), 2), 0.5,color='dodgerblue', label='Human')
    plt.bar('% char.\nTot. : '+str(ql+hl), round(ql*100/(ql+hl), 2), color='blue')
    plt.bar('% char.\nTot. : '+str(ql+hl), round(hl*100/(ql+hl), 2), 0.5, color='dodgerblue')
    plt.bar('% word.\nTot. : '+str(qw+hw), round(qw*100/(qw+hw), 2), color='blue')
    plt.bar('% word.\nTot. : '+str(qw+hw), round(hw*100/(qw+hw), 2), 0.5, color='dodgerblue')
    plt.bar('% question\nTot. : '+str(qqm+hqm), round(qqm*100/(qqm+hqm), 2), color='blue')
    plt.bar('% question\nTot. : '+str(qqm+hqm), round(hqm*100/(qqm+hqm), 2), 0.5, color='dodgerblue')
    plt.legend()
    plt.ylim(0, 100)
    plt.tight_layout()
    return plt


