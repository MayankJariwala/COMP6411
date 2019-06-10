%% Mayank Jariwala - 40075419
-module(exchange).

%% ====================================================================
%% API functions
%% ====================================================================
-export([start/0,caller/1]).
-define(MASTER_TIMEOUT,1500).

start() ->
    {ok, Pairs} = file:consult("calls.txt"),
    io:format("~s.~n",["*** Calls to be made ***"]),
    [io:format("~w: ~w.~n",[Sender,Receivers]) || {Sender, Receivers} <- Pairs],
    io:format("~s",["\n"]),
    Filtered_list = maps:from_list(Pairs),
    M_id = self(),
    ets:new(my_table, [named_table, protected, set, {keypos, 1}]),
	maps:fold(fun(K, V, ok) ->
    	P_id = spawn(calling,messagePassing,[K,V,M_id]),
   	 	ets:insert(my_table, {P_id,K}),
		io:format("")
	end,ok, Filtered_list),
	caller(M_id),
	ok.


caller(M_id) ->    
    receive
		{intro,Sender,Receiver,Ms} ->
			io:format("~w received intro message from ~w [~w]~n",[Receiver,Sender,Ms]),
			caller(M_id);
		{reply,Sender,Receiver,Ms} ->
			io:format("~w received reply message from ~w [~w]~n",[Sender,Receiver,Ms]),
			caller(M_id)

		after ?MASTER_TIMEOUT ->
			io:format("Master has received no replies for ~.1f seconds, ending....~n",[?MASTER_TIMEOUT/1000]),
			halt(0)			
	end.