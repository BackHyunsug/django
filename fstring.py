fstring.py

def view(request, id):
sql=f"update board_board set hit=hit+1 where id={id}"
   = "update board_board set hit=hit+1 where id={}".format(id)
   = "update board_board set hit=hit+1 where id=%d" % (id)
   = "update board_board set hit=hit+1 where id=" + str(id)

   우리목적
    "update board_board set hit=hit+1 where id=15"
0