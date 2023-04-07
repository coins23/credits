import codeToCourse from "../courses";
import { getRequirementAndDictionaryFromJSON } from "../Requirements";
import coins23_0 from "./coins23.json";

const requirementAndDictionaryPairs = new Map([
  [
    "coins23",
    {
      id: "coins23",
      name: "情報科学類 / 2023年度入学",
      ...getRequirementAndDictionaryFromJSON(coins23_0, codeToCourse),
    },
  ],
]);

export default requirementAndDictionaryPairs;
