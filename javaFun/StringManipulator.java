public class StringManipulator{
    public String trimAndConcat(String str1, String str2){
        return str1.trim() + str2.trim();
    } 
}
public class StringManipulator{
    public Integer getIndexOrNull(String str3, char letter){
        int index = str3.indexOf(letter);
        if(index == -1){
            return null;
        }
        else {
            return index;
        }
    }
}

public class StringManipulator{
    public Integer getIndexOrNull(String str4, String str5){
        int index = str4.indexOf(str5);
        if(index == -1){
            return null;
        }
        else{
            return index;
        }
    }
}

public class StringManipulator{
    public String concatSubstring(String str6, int a1, int b1, String str7){
        String stringy = str6.substring(a1, b1) + str7;
        return stringy;
    }
}