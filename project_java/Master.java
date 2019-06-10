//Mayank Jariwala - 40075419
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Master implements Runnable {
	
	HashMap<String,List<String>> hashmap = new HashMap<>();
	HashMap<String,Process> Objectmap = new HashMap<>();
	public Master(){};
	static int threadsCompleted = 0;
	static int hashMapSize = 0;

	//Parameterized Constructor
	Master(HashMap<String,List<String>> hashmap){
		this.hashmap = hashmap;
		for (Map.Entry<String, List<String>> entry : hashmap.entrySet()) {
			try {
				Process p = new Process();
				Objectmap.put(entry.getKey(),p);
			}
			catch(Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	@Override
	public synchronized void run() {
		hashMapSize = hashmap.size();
		for (Map.Entry<String, List<String>> entry : hashmap.entrySet()) {
			try {
				Thread t1 = new Thread(new Process(entry.getKey(),entry.getValue(),Objectmap),entry.getKey());
			    t1.start();
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	public void printMessage(Messages message) {
		System.out.println(message.getSender() + " received " 
					+ message.getType() + " message from " + message.getReceiver()
					+ " [" + message.getTime() + "]");
	}
	
	public synchronized void monitorsThread() throws InterruptedException{
		threadsCompleted++;
		if(hashMapSize == threadsCompleted) {
			wait(1500);
			System.out.println("Master has received no replies for 1.5 seconds, ending...");
		}
	}
}
