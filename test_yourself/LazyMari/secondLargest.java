import java.util.Arrays;

public class secondLargest {
	public static double secondMax(Data data){
		double max = Double.MIN_VALUE;
		double max2 = Double.MIN_VALUE;
		for(int i=0; i<data.data.length;i++){
			if(data.data[i]>max){
				max2 = data.data[i];
				if(max2>max){
					double temp;
					temp = max;
					max = max2;
					max2 = temp;
				}
			}
		}
		return max2;
	}
	public static void main(String[] args) {
		Data data = new Data();
		long start = System.currentTimeMillis();
		System.out.println(secondMax(data));
		System.out.println("Time for my method:");
		System.out.println(System.currentTimeMillis() - start);
		
		long start2 = System.currentTimeMillis();
		Arrays.sort(data.data);
		System.out.println(data.data[data.data.length-2]);
		System.out.println("Time for array sort:");
		System.out.println(System.currentTimeMillis() - start2);
		

	}

}
