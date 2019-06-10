%% Mayank Jariwala - 40075419
-module(calling).

%% ====================================================================
%% API functions
%% ====================================================================
-export([messagePassing/3,iterateLoop/3,caller/1]).
-define(PROCESS_TIMEOUT,1000).

messagePassing(K,V,M_id) ->
	iterateLoop(K,V,self()),
	caller(M_id).

caller(M_id) ->
	receive
		{request,K,Item,P_id,Ms} ->
			timer:sleep(100),
			M_id ! {intro,K,Item,Ms},
			P_id ! {response,M_id,K,Item,Ms};
		{response,M_id,Sender,Receiver,Ms} ->
			timer:sleep(100),
			M_id ! {reply,Sender,Receiver,Ms}
		   
		
		after ?PROCESS_TIMEOUT ->
			[{_, Host}] = ets:lookup(my_table,self()),
			io:format("Process ~w has received no calls for ~w second, ending...~n",[Host,?PROCESS_TIMEOUT div 1000]),
			exit(normal)
	end,
	caller(M_id).

iterateLoop(K,V,P_id) ->
	register(K,P_id),
	lists:foreach(fun (Item) ->
		{_,_,Ms} = erlang:now(),
		P_id ! {request,K,Item,P_id,Ms}
	end, V).	
