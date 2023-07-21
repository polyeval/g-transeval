<?php
// Write the declarations here

// Write the target function here

// End here

function serializeArray($obj): string
{
    $sorted = $obj;
    ksort($sorted);
    $arrayStr = "{";
    foreach ($sorted as $key => $value) {
        $arrayStr .= serializeObj($key);
        $arrayStr .= ":";
        $arrayStr .= serializeObj($value);
        $arrayStr .= ",";
    }
    $arrayStr[-1] = "}";
    return $arrayStr;
}

function serializeObj($obj): string
{
    if (is_null($obj)) {
        return "null";
    }
    if (is_int($obj)) {
        return strval($obj);
    }
    if (is_float($obj)) {
        return sprintf("%.6f", $obj);
    }
    if (is_bool($obj)) {
        return strval($obj);
    }
    if (is_string($obj)) {
        return "\"" . $obj . "\"";
    }
    if (is_array($obj)) {
        return serializeArray($obj);
    }
    throw new Exception("Unrecognized Type!");
}

function areEquivalent($o1, $o2): bool
{
    return serializeObj($o1) == serializeObj($o2);
}

function start()
{
    $ret = false;
    $total = 0;
    $count = 0;
    // Write the unit tests here
    
    // End here
    if ($count == $total) {
        echo "All Passed!";
    } else {
        echo "Compilation Passed!";
    }
}

start();
