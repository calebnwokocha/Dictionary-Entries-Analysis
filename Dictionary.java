import org.json.JSONObject;
import org.json.JSONTokener;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class Dictionary {

    // Global cache to store word definitions
    private static final Map<String, String> definitionCache = new HashMap<>();

    public static void main(String[] args) {
        // File path to the dictionary JSON file
        String filePath = "dictionary.json";

        // Load the dictionary data
        JSONObject dictionary = loadDictionary(filePath);

        // Continuous interaction loop
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine();
            System.out.println("Providing definitions for input...");
            provideDefinitions(userInput, dictionary, 0, 3);
        }
    }

    private static JSONObject loadDictionary(String filePath) {
        try (FileInputStream inputStream = new FileInputStream(filePath)) {
            JSONTokener tokener = new JSONTokener(inputStream);
            return new JSONObject(tokener);
        } catch (IOException e) {
            e.printStackTrace();
            return new JSONObject();
        }
    }

    private static String getDefinition(String word, JSONObject dictionary) {
        word = word.replaceAll("\\p{Punct}", "").toLowerCase();
        if (definitionCache.containsKey(word)) {
            return definitionCache.get(word);
        }
        if (dictionary.has(word)) {
            String definition = dictionary.getString(word);
            definitionCache.put(word, definition);
            return definition;
        }
        return word;
    }

    private static void provideDefinitions(String text, JSONObject dictionary, int depth, int maxDepth) {
        if (depth > maxDepth) {
            return;
        }

        String[] words = text.split("\\s+");
        int numWords = words.length;

        // Randomly select k words
        Random random = new Random();
        int k = Math.min(random.nextInt(numWords) + 1, numWords);
        System.out.printf("Selected %d words for definitions.%n", k);

        Set<Integer> selectedPositions = new HashSet<>();
        while (selectedPositions.size() < k) {
            selectedPositions.add(random.nextInt(numWords));
        }

        // Combine selected words with their definitions
        StringBuilder combinedOutput = new StringBuilder();
        for (int i = 0; i < numWords; i++) {
            if (selectedPositions.contains(i)) {
                combinedOutput.append(getDefinition(words[i], dictionary));
            } else {
                combinedOutput.append(words[i]);
            }
            combinedOutput.append(" ");
        }

        String output = combinedOutput.toString().trim();

        // If at the maximum depth, return the definitions
        if (depth == maxDepth) {
            System.out.println("AI: " + output);
            //TextToSpeech.speak(output);
            return;
        }

        // Recursively call the function with the new input
        provideDefinitions(output, dictionary, depth + 1, maxDepth);
    }
}
