// Write the declarations here
import java.util.*;
import java.util.stream.*;
import java.lang.reflect.Array;

class Test {
  private static String serializeList(List obj) {
    StringBuilder listStr = new StringBuilder("[");
    for (Object item : obj) {
      listStr.append(serializeObj(item));
      listStr.append(",");
    }
    listStr.setCharAt(listStr.length() - 1, ']');
    return listStr.toString();
  }

  private static String serializeArray(Object obj) {
    StringBuilder listStr = new StringBuilder("[");
    for (int i = 0; i < Array.getLength(obj); i++) {
      listStr.append(serializeObj(Array.get(obj, i)));
      listStr.append(",");
    }
    listStr.setCharAt(listStr.length() - 1, ']');
    return listStr.toString();
  }

  private static String serializeDict(Map obj) {
    var m = new TreeMap<Object, Object>();
    for (Object item : obj.entrySet()) {
      m.put(((Map.Entry) item).getKey(), ((Map.Entry) item).getValue());
    }
    StringBuilder mapStr = new StringBuilder("{");
    for (var item : m.entrySet()) {
      mapStr.append(serializeObj(item.getKey()));
      mapStr.append(":");
      mapStr.append(serializeObj(item.getValue()));
      mapStr.append(",");
    }
    mapStr.setCharAt(mapStr.length() - 1, '}');
    return mapStr.toString();
  }

  private static String serializeObj(Object obj) {
    if (obj == null) {
      return "null";
    }
    if (obj instanceof Integer) {
      return String.valueOf(obj);
    }
    if (obj instanceof Double) {
      return String.format("%.6f", obj);
    }
    if (obj instanceof Boolean) {
      return String.valueOf(obj);
    }
    if (obj instanceof Character) {
      return "'" + String.valueOf(obj) + "'";
    }
    if (obj instanceof String) {
      return "\"" + obj + "\"";
    }
    if (obj.getClass().isArray()){
      return serializeArray(obj);
    }
    if (obj instanceof List<?>) {
      return serializeList((List) obj);
    }
    if (obj instanceof Map<?, ?>) {
      return serializeDict((Map) obj);
    }
    throw new RuntimeException("Unrecognized Type!");
  }

  public static boolean areEquivalent(Object o1, Object o2) {
    System.out.println(serializeObj(o1)+" "+serializeObj(o2));
    return serializeObj(o1).equals(serializeObj(o2));
  }

  public static
  // Write the target function here

  // End here

  public static void start() {
    boolean ret;
    int total = 0;
    int count = 0;
    // Write the unit tests here

    // End here
    if (count == total) {
      System.out.println("All Passed!");
    } else {
      System.out.println("Compilation Passed!");
    }
  }

  public static void main(String[] args) {
    start();
  }
}
