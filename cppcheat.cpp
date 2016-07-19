
#include <iostream>
#include <ctime>
#include <string>


// in default namespace
// do not use macros in CPP neither uppercase
int const MINUTES_PER_HOUR = 60;

// enum
/*enum class PartitionedBy : char {None, Month, Year};

void enumUsage() {
  PartitionedBy pb = PartitionedBy::Month;
  if (pb == PartitionedBy::Month)
    std::cout << "partitioned by month" << std::endl;
}*/

void times() {
  //#include <ctime>
  tm from_tm;
  time_t from;// some init
  localtime_r(&from, &from_tm);
  // do not use localtime, because it stores the value into the internal buffer and can be overwritten
  from_tm.tm_mon; // 0-11
  from_tm.tm_year;// years since 1900
}

int main(int argc, char** argv) {
  const char *date_str = "2016-01-22 00:00:00";
  // init is necessary - without it there will be garbage and 
  struct tm date_tm = {0};  // may cause warning in gcc because of unitilialised other attributes
  strptime(date_str, "%Y-%m-%d %h:%M:%s", &date_tm);
  time_t dt = mktime(&date_tm);  // t is now your desired time_t
  std::cout << date_tm.tm_year << std::endl;

  char date_iso[11];  // 11th byte for ending \0
  tm date_tm2;
  localtime_r(&dt, &date_tm2);
  strftime(date_iso, sizeof(date_iso), "%Y-%m-%d", &date_tm2);
  std::cout << date_iso << std::endl;
}
