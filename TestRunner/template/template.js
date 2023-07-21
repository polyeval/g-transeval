// Write the declarations here

// Write the target function here

// End here

function serializeList(obj) {
  listStr = "[";
  for (const item of obj) {
    listStr += serializeObj(item);
    listStr += ",";
  }
  listStr = listStr.slice(0, listStr.length - 1) + "]";
  return listStr;
}

function serializeDict(obj) {
  sorted = new Map([...obj.entries()].sort());
  dictStr = "{";
  for (const [key, value] of sorted) {
    dictStr += serializeObj(key);
    dictStr += ":";
    dictStr += serializeObj(value);
    dictStr += ",";
  }
  dictStr = dictStr.slice(0, dictStr.length - 1) + "}";
  return dictStr;
}

function serializeObj(obj) {
  if (typeof obj == "undefined") {
    return "null";
  }
  if (typeof obj == "number") {
    return obj.toFixed(6);
  }
  if (typeof obj == "boolean") {
    return obj.toString();
  }
  if (typeof obj == "string") {
    return '"' + obj + '"';
  }
  if (Array.isArray(obj)) {
    return serializeList(obj);
  }
  if (obj instanceof Map) {
    return serializeDict(obj);
  }
  throw new Exception("Unrecognized Type!");
}

function areEquivalent(o1, o2) {
  console.log(serializeObj(o1) +" "+ serializeObj(o2) )
  return serializeObj(o1) == serializeObj(o2);
}

function start() {
  ret = false;
  total = 0;
  count = 0;
  // Write the unit tests here

  // End here
  if (count == total) {
    console.log("All Passed!");
  } else {
    console.log("Compilation Passed!");
  }
}

start();
