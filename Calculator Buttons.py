button1 = Button(backg,font= ("arial",15),text=' 1 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("1"), height=3, width=8)
button2 = Button(backg,font= ("arial",15),text=' 2 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("2"), height=3, width=8)
button3 = Button(backg,font= ("arial",15),text=' 3 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("3"), height=3, width=8)
button4 = Button(backg,font= ("arial",15),text=' 4 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("4"), height=3, width=8)
button5 = Button(backg,font= ("arial",15),text=' 5 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("5"), height=3, width=8)
button6 = Button(backg,font= ("arial",15),text=' 6 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("6"), height=3, width=8)
button7 = Button(backg,font= ("arial",15),text=' 7 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("7"), height=3, width=8)
button8 = Button(backg,font= ("arial",15),text=' 8 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("8"), height=3, width=8)
button9 = Button(backg,font= ("arial",15),text=' 9 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("9"), height=3, width=8)
button0 = Button(backg,font= ("arial",15),text=' 0 ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("0"), height=3, width=8)
buttonadd = Button(backg,font= ("arial",15),text=' + ',bd=1,relief='ridge',fg='black', bg='#ffaa00',command=lambda: Click("+"), height=3, width=8)
buttonsub = Button(backg,font= ("arial",15),text=' - ',bd=1,relief='ridge',fg='black', bg='#ffaa00',command=lambda: Click("-"), height=3, width=8)
buttonmulti = Button(backg,font= ("arial",15),text=' x ',bd=1,relief='ridge',fg='black', bg='#ffaa00',command=lambda: Click("*"), height=3, width=8)
buttondiv = Button(backg,font= ("arial",15),text=' ÷ ',bd=1,relief='ridge',fg='black', bg='#ffaa00',command=lambda: Click("/"), height=3, width=8)
buttondec = Button(backg,font= ("arial",15),text=' . ',bd=1,relief='ridge',fg='black', bg='white',command=lambda: Click("."), height=3, width=8)
buttonclear = Button(backg,font= ("arial",15),text=' C ',bd=1,relief='ridge',fg='black', bg='white',command=Clear, height=3, width=8)
buttonequal = Button(backg,font= ("arial",15),text=' =',bd=1,relief='ridge',fg='black', bg='#ffaa00',command=evaluate, height=3, width=8)
buttondel = Button(backg,font= ("arial",15),text='DEL',bd=1,relief='ridge',fg='black', bg='white',command=delete, height=3, width=8)

buttonsqr = Button(backg,font= ("arial",15),text='√',bd=1,relief='ridge',fg='black', bg='white',height=3, width=8)
buttonsqr.bind("<Button-1>",sc)

buttonpi = Button(backg,font= ("arial",15),text='π',bd=1,relief='ridge',fg='black', bg='white',height=3, width=8)
buttonpi.bind("<Button-1>",sc)

buttonclear.grid(row=1, column=0)
buttondel.grid(row=1, column=1)
buttonsqr.grid(row=1, column=2)
buttondiv.grid(row=1, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
buttonmulti.grid(row=2, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonsub.grid(row=3, column=3)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
buttonadd.grid(row=4, column=3)


button0.grid(row=5, column=0)
buttondec.grid(row=5, column=1)

buttonpi.grid(row=5, column=2)
buttonequal.grid(row=5, column=3)