import java.util.*;

class RandomizedSet {

    private ArrayList<Integer> list;
    private HashMap<Integer, Integer> map;
    private Random random;

    public RandomizedSet() {
        list = new ArrayList<>();
        map = new HashMap<>();
        random = new Random();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) {
            return false;
        }

        // Add value to the end
        list.add(val);

        // Store its index
        map.put(val, list.size() - 1);

        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        }

        // Index of the element to remove
        int index = map.get(val);

        // Get the last element
        int lastElement = list.get(list.size() - 1);

        // Move last element into the position of val
        list.set(index, lastElement);

        // Update last element's index
        map.put(lastElement, index);

        // Remove last element
        list.remove(list.size() - 1);

        // Remove val from map
        map.remove(val);

        return true;
    }
    
    public int getRandom() {
        int index = random.nextInt(list.size());
        return list.get(index);
    }
}