//Mayank Jariwala - 40075419
import java.util.HashMap;
import java.util.List;

public class Process implements Runnable {
	
	String currentKey;
	List<String> FriendList;
	HashMap<String,Process> Objectmap;
	
	//Default Constructor
	public Process(){};
	
	//Initiate Constructor
	Process(String Key,List<String> FriendList,HashMap<String,Process> Objectmap){
		currentKey = Key;
		this.Objectmap = Objectmap;
		this.FriendList = FriendList;
	};
	
	@Override
	public synchronized void run() {
		try {
			this.iterateLoop(currentKey,FriendList,Objectmap);
			wait(1000);
			System.out.println("Process " + Thread.currentThread().getName() + " has received no calls for 1 second, ending... ");
			new Master().monitorsThread();
		}
		catch(InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public void iterateLoop(String key,List<String> FriendsList,HashMap<String,Process> Objectmap) {
		try {
			for (String friend : FriendsList) {
				Thread.sleep(100);
				Long time = System.nanoTime()/1000;
				Objectmap.get(key).sendMessage(key,friend,"intro",Objectmap,time);
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public void sendMessage(String Sender,String Receiver,String Type,HashMap<String,Process> Objectmap,Long Time){
		try {
			new Master().printMessage(new Messages(Sender,Receiver,Type,Time));
			Thread.sleep(100);
			Objectmap.get(Receiver).receiveMessage(Receiver,Sender,"reply",Time);
		}
		catch(InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public void receiveMessage(String Sender,String Receiver,String Type,Long Time){
		new Master().printMessage(new Messages(Sender,Receiver,Type,Time));
	}
}
