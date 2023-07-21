double DistinctOddRatio ( List < int > numbers ) { int distinctCount = numbers . Distinct ( ) . Count ( ) ; int distinctOddCount = numbers . Distinct ( ) . Count ( n => n % 2 == 1 ) ; return ( double ) distinctOddCount / distinctCount ; } 
int CompareSum ( List < int > numbers , List < string > words ) { int intSum = numbers . Sum ( ) ; int wordLengthSum = words . Sum ( w => w . Length ) ; if ( intSum < wordLengthSum ) { return - 1 ; } if ( intSum > wordLengthSum ) { return 1 ; } return 0 ; } 
bool AllLongerThan ( List < string > shortWords , List < string > longWords ) { int maxOfShort = shortWords . Max ( w => w . Length ) ; int minOfLong = longWords . Min ( w => w . Length ) ; return minOfLong > maxOfShort ; } 
int CompareOddEvenRange ( List < int > numbers ) { int rangeOdd = numbers . Where ( n => n % 2 == 1 ) . Max ( ) - numbers . Where ( n => n % 2 == 1 ) . Min ( ) ; int rangeEven = numbers . Where ( n => n % 2 == 0 ) . Max ( ) - numbers . Where ( n => n % 2 == 0 ) . Min ( ) ; if ( rangeOdd < rangeEven ) { return - 1 ; } if ( rangeOdd > rangeEven ) { return 1 ; } return 0 ; } 
double AverageDistinctLength ( List < string > words ) { double averageLen = words . Distinct ( ) . Average ( w => w . Length ) ; return averageLen ; } 
int WithDrawBalance ( int start , List < int > withdrawals ) { int end = withdrawals . Aggregate ( start , ( balance , nextWithdrawal ) => nextWithdrawal <= balance ? balance - nextWithdrawal : balance ) ; return end ; } 
string FirstShortAndStartsWithO ( List < string > words ) { string matchedElement = words . Where ( w => w . Length < 5 ) . FirstOrDefault ( w => w [ 0 ] == 'o' , "" ) ; return matchedElement ; } 
int BigNumberAtIndex ( List < int > numbers , int index ) { int targetNum = numbers . Where ( n => n > 5 ) . ElementAt ( index ) ; return targetNum ; } 
bool ContainsSquareInRange ( int rangeStart , int rangeLength ) { bool containsSquare = Enumerable . Range ( rangeStart , rangeLength ) . Any ( n => Math . Pow ( ( int ) Math . Sqrt ( n ) , 2 ) == n ) ; return containsSquare ; } 
Dictionary < int , List < int > > GroupNumbersByMod ( List < int > numbers , int mod ) { var numberGroups = numbers . GroupBy ( n => n % mod ) . ToDictionary ( g => g . Key , g => g . ToList ( ) ) ; return numberGroups ; } 
Dictionary < char , List < string > > GroupWordsByFirstChar ( List < string > words ) { var wordGroups = words . GroupBy ( w => w [ 0 ] ) . ToDictionary ( g => g . Key , g => g . ToList ( ) ) ; return wordGroups ; } 
List < string > OrderByLengthAndDescending ( List < string > words ) { var sortedWords = words . OrderBy ( w => w . Length ) . ThenByDescending ( w => w ) . ToList ( ) ; return sortedWords ; } 
List < string > OrderFirstCharDescendingReverse ( List < string > words ) { var sortedWords = words . OrderByDescending ( w => w [ 0 ] ) . ThenBy ( w => w ) . Reverse ( ) . ToList ( ) ; return sortedWords ; } 
List < int > GetSubListOfNegative ( List < int > numbers , int start , int length ) { List < int > subList = numbers . Skip ( start ) . Where ( n => n < 0 ) . Take ( length ) . ToList ( ) ; return subList ; } 
List < int > GetPositiveSequence ( List < int > numbers ) { List < int > subSequence = numbers . SkipWhile ( n => n <= 0 ) . TakeWhile ( n => n >= 0 ) . ToList ( ) ; return subSequence ; } 
List < int > GetLargerThanIndexSequence ( List < int > numbers ) { List < int > subSequence = Enumerable . Range ( 0 , numbers . Count ) . SkipWhile ( i => numbers [ i ] < i ) . TakeWhile ( i => numbers [ i ] >= i ) . Select ( i => numbers [ i ] ) . ToList ( ) ; return subSequence ; } 
List < string > RearrangeWordByIndexes ( List < string > words , List < int > indexes ) { List < int > newIndexes = indexes . Where ( n => n >= words . Count ) . Select ( n => n % words . Count ) . ToList ( ) ; List < string > newWords = newIndexes . Select ( n => words [ n ] ) . ToList ( ) ; return newWords ; } 
List < List < string > > GetWordsUpperLower ( List < string > words ) { var upperLowerWords = words . Select ( w => new List < string > { w . ToUpper ( ) , w . ToLower ( ) } ) . ToList ( ) ; return upperLowerWords ; } 
List < bool > SelectIfInPlace ( List < int > numbers ) { List < bool > numsInPlace = numbers . Select ( ( num , index ) => num == index ) . ToList ( ) ; return numsInPlace ; } 
List < List < int > > SelectPairs ( List < int > numbersA , List < int > numbersB ) { var pairs = numbersA . SelectMany ( a => numbersB . Where ( b => a < b ) , ( a , b ) => new List < int > { a , b } ) . ToList ( ) ; return pairs ; } 
List < string > StringCrossJoin ( List < string > endWords , List < string > beginWords ) { List < string > crossStrings = beginWords . Join ( endWords , b => b [ 0 ] , e => e [ ^ 1 ] , ( b , e ) => e + " " + b ) . ToList ( ) ; return crossStrings ; } 
int ElementsContainSubword ( List < string > words , string subword ) { if ( words . Take ( 5 ) . All ( w => w . Contains ( subword ) ) ) { return 1 ; } if ( words . Take ( 5 ) . Any ( w => w . Contains ( subword ) ) ) { return 0 ; } return - 1 ; } 
List < int > ConcatLargeNumbers ( List < int > numbersA , List < int > numbersB , int flag ) { List < int > allNumbers = numbersA . Where ( n => n > flag ) . Concat ( numbersB . Where ( n => n > flag ) ) . ToList ( ) ; return allNumbers ; } 
int DotProduct ( List < int > vectorA , List < int > vectorB ) { int dotProduct = vectorA . Zip ( vectorB , ( a , b ) => a * b ) . Sum ( ) ; return dotProduct ; } 
List < int > SetDifference ( List < int > setA , List < int > setB ) { var difference = setA . Union ( setB ) . Except ( setA . Intersect ( setB ) ) . ToList ( ) ; difference . Sort ( ) ; return difference ; } 