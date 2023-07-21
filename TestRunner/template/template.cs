// Write the declarations here
using System;
using System.Text;
using System.Collections;
using System.Collections.Generic;

Test.Start();

class Test
{
    private static string SerializeObj(dynamic obj)
    {
        if (obj == null)
        {
            return "null";
        }
        if (obj is int)
        {
            return obj.ToString();
        }
        if (obj is double)
        {
            return string.Format("{0:N6}", obj);
        }
        if (obj is bool)
        {
            return obj.ToString();
        }
        if (obj is char)
        {
            return "'" + obj + "'";
        }
        if (obj is string)
        {
            return "\"" + obj + "\"";
        }
        if (obj.GetType().GetGenericTypeDefinition().IsAssignableFrom(typeof(List<>)))
        {
            return SerializeList((IList)(object)obj);
        }
        if (obj.GetType().GetGenericTypeDefinition().IsAssignableFrom(typeof(Dictionary<,>)))
        {
            return SerializeDict((IDictionary)(object)obj);
        }
        throw new Exception("Unrecognized Type!");
    }

    private static string SerializeList(IList obj)
    {
        StringBuilder listStr = new StringBuilder("[");
        foreach (object item in obj)
        {
            listStr.Append(SerializeObj(item));
            listStr.Append(",");
        }
        listStr[^1] = ']';
        return listStr.ToString();
    }

    private static string SerializeDict(IDictionary obj)
    {
        var m = new SortedDictionary<object, object>();
        foreach (DictionaryEntry item in obj)
        {
            m[item.Key] = item.Value;
        }
        StringBuilder dictStr = new StringBuilder("{");
        foreach (var (key, value) in m)
        {
            dictStr.Append(SerializeObj(key));
            dictStr.Append(":");
            dictStr.Append(SerializeObj(value));
            dictStr.Append(",");
        }
        dictStr[^1] = '}';
        return dictStr.ToString();
    }

    public static bool AreEquivalent(dynamic o1, dynamic o2)
    {
        Console.WriteLine(SerializeObj(o1)+" "+SerializeObj(o2));
        return SerializeObj(o1).Equals(SerializeObj(o2));
    }

    public static
    // Write the target function here

    // End here

    public static void Start()
    {
        bool ret;
        int total = 0;
        int count = 0;
        // Write the unit tests here

        // End here
        if (count == total)
        {
            Console.WriteLine("All Passed!");
        }
        else
        {
            Console.WriteLine("Compilation Passed!");
        }
    }
}
