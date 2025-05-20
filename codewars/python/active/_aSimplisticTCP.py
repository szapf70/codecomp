# https://www.codewars.com/kata/54acc128329e634e9a000362/train/python
# A Simplistic TCP Finite State Machine (FSM)

def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always
    m = {
            'CLOSED' :      {
                                'APP_PASSIVE_OPEN' : 'LISTEN',
                                'APP_ACTIVE_OPEN' : 'SYN_SENT'},
            'LISTEN' :      {
                                'RCV_SYN' : 'SYN_RCVD',
                                'APP_SEND' : 'SYN_SENT',
                                'APP_CLOSE' : 'CLOSED'},
            'SYN_RCVD' :    {
                                'APP_CLOSE' : "FIN_WAIT_1",
                                'RCV_ACK' : 'ESTABLISHED'},
            'SYN_SENT' :    {
                                'RCV_SYN' : 'SYN_RCVD',
                                'RCV_SYN_ACK' : 'ESTABLISHED',
                                'APP_CLOSE' : 'CLOSED'},
            'ESTABLISHED' : {
                                'APP_CLOSE' : 'FIN_WAIT_1',
                                'RCV_FIN' : 'CLOSE_WAIT'},
            'FIN_WAIT_1' :  {
                                'RCV_FIN' : 'CLOSING',
                                'RCV_FIN_ACK' : 'TIME_WAIT',
                                'RCV_ACK' : 'FIN_WAIT_2'},
            'CLOSING' :     {
                                'RCV_ACK' : 'TIME_WAIT'},
            'FIN_WAIT_2' :  {
                                'RCV_FIN' : 'TIME_WAIT'},
            'TIME_WAIT' :   {
                                'APP_TIMEOUT' : 'CLOSED'},
            'CLOSE_WAIT' :  {
                                'APP_CLOSE' : 'LAST_ACK'},
            'LAST_ACK' :    {
                                'RCV_ACK' : 'CLOSED'}                                                                                
        }
    
    for e in events:
        if state in m.keys():
            pre = m[state]
            if e in pre.keys():
                state = pre[e]
            else:
                return 'ERROR'
        else:    
            return 'ERROR'
    
    return state


#print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN"]), "CLOSE_WAIT")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN","RCV_ACK"]), "ESTABLISHED")    
#print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"]), "LAST_ACK")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN"]), "SYN_SENT")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","APP_SEND"]), "ERROR")
print(traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN","RCV_ACK",   "APP_CLOSE"]),"FIN_WAIT_1")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN","RCV_ACK"]), "ESTABLISHED")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN"]), "SYN_RCVD")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN"]), "LISTEN")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN","APP_CLOSE"]), "CLOSED")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN","APP_CLOSE","RCV_FIN","RCV_ACK"]), "TIME_WAIT")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN","APP_CLOSE","RCV_FIN","RCV_ACK","APP_TIMEOUT"]), "CLOSED")
#print(traverse_TCP_states(["RCV_SYN","RCV_ACK","APP_CLOSE"]),"ERROR")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN","APP_CLOSE","RCV_ACK"]), "FIN_WAIT_2")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN"]), "CLOSE_WAIT")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"]), "LAST_ACK")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN"]), "SYN_SENT")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN","APP_CLOSE"]), "CLOSED")
#print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","APP_CLOSE"]), "FIN_WAIT_1")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_PASSIVE_OPEN"]), "ERROR")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","RCV_FIN_ACK","APP_TIMEOUT","APP_ACTIVE_OPEN","RCV_SYN","APP_CLOSE","RCV_FIN","RCV_ACK"]), "TIME_WAIT")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","RCV_SYN"]), "ERROR")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN","APP_CLOSE","RCV_SYN"]), "ERROR")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE"]), "FIN_WAIT_1")
#print(traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","RCV_FIN"]), "CLOSING")

