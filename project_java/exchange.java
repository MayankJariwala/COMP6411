//Mayank Jariwala - 40075419
import java.util.*;
import java.io.*;

class Driver{
	
	//Default Constructor
	Driver(){};
	public static void main(String[] args) throws IOException {
		File file = new File("calls.txt");
		try {
			Driver driver = new Driver();
			BufferedReader br = new BufferedReader(new FileReader(file));
			LinkedHashMap<String,List<String>> hashmap = new LinkedHashMap<>();
			String st;
			while ((st = br.readLine()) != null) {
			  String[] value = st.substring(st.indexOf("{") + 1, st.indexOf("}")).split(",",2);
			  List<String> myList = new ArrayList<String>(Arrays.asList(driver.distributeStringArr(value[1])));
			  hashmap.put(value[0],myList);
			}
			driver.printJustFilesData(hashmap);
			Thread t = new Thread(new Master(hashmap),"Master");
			t.start();
			br.close();
			
		} catch (FileNotFoundException e) {
			// File Not Found Exception Thrown
			e.printStackTrace();
		}
	}
	
	public String[] distributeStringArr(String st) {
		String[] value = st.substring(st.indexOf("[") + 1, st.indexOf("]")).split(",");
		return value;
	}
	
	public void printJustFilesData(LinkedHashMap<String,List<String>> hashmap){
		System.out.println("*** Calls to be Made ***");
		for (Map.Entry<String, List<String>> entry : hashmap.entrySet()) {
			System.out.println(entry.getKey() + " : " + entry.getValue());
		}
		System.out.println("");
	}
	
}