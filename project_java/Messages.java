//Mayank Jariwala - 40075419
public class Messages {
	private String sender,receiver,type;
	private Long Time;
	
	public Messages(String sender,String reciever,String type,Long Time) {
		this.sender = sender;
		this.receiver = reciever;
		this.type = type;
		this.Time = Time;
	}

	public String getSender() {
		return sender;
	}
	
	public Long getTime() {
		return Time;
	}
	
	public String getReceiver() {
		return receiver;
	}

	public String getType() {
		return type;
	}
	
	
}
