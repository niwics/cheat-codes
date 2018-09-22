import java.io.File;
import java.io.FileFilter;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Month;
import java.time.format.TextStyle;
import java.util.Arrays;
import java.util.Locale;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class JavaCheat {

    private int attribute;

    public JavaCheat() {
        // calling the overloaded constructor (preferred style is calling from the non-parametric the most complex one)
        this(1);
    }

    /**
     * Overloading the constructor.
     * @param attribute
     */
    public JavaCheat(int attribute) {
        this.attribute = attribute;
    }

    public static void arrays() {
        String[] players = new String[] {"Roger", "Rafa", "Nole", "Andy"};

        // print the array
        System.out.println(Arrays.toString(players));
        // print with possible subarrays
        System.out.println(Arrays.deepToString(players));
    }

    public static void dates() {
        // get czech name of month
        // see discussion (in czech) https://forum.root.cz/index.php?topic=10375.0
        String january = Month.JANUARY.getDisplayName(TextStyle.FULL_STANDALONE, new Locale("cs"));
        // or
        january = Month.of(1).getDisplayName(TextStyle.FULL_STANDALONE, new Locale("cs"));
        System.out.println(january);    // leden
    }

    public static void filesystem() {

        // listing the content of the dir
        // filter just subdirectories
        File[] subdirs = new File("/your/path/").listFiles(new FileFilter() {
            @Override
            public boolean accept(File file) {
                return file.isDirectory();
            }
        });
        // or since Java 8 - simple dir filter

        File[] subdirs2 = new File("/your/path/").listFiles(File::isDirectory);

        // merging file paths
        Path path = Paths.get("foo", "bar", "baz.txt");
        // using File class
        File subDirectory = new File("/tmp/my-dir");
        File fileInDirectory = new File(subDirectory, "baz.txt");

        // splitting file paths from string
        String pathString = path.toString();
        String[] subDirs = pathString.split(Pattern.quote(File.separator));
        // or to get just the parent dir path:
        fileInDirectory.getParentFile();

        // create all directories from the path
        File dir = new File("/tmp/my/dir1/dir2");
        dir.mkdirs();
    }

    public static void regexps(){
        String s = "Müller";

        // since Java 7
        Pattern p = Pattern.compile("^\\w+$", Pattern.UNICODE_CHARACTER_CLASS);
        Matcher m = p.matcher(s);
        if (m.find()) {
            System.out.println(m.group());
        } else {
            System.out.println("not found");
        }
    }

    // optional parameters are not allowed - use overloading of methods instead
    // how to call constructor from another constructor?
    public static void main(String[] args) {
        System.out.println("Java cheat codes");
    }
}
