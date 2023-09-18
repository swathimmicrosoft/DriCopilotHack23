import { Example } from "./Example";

import styles from "./Example.module.css";

export type ExampleModel = {
    text: string;
    value: string;
};

const EXAMPLES: ExampleModel[] = [
    {
        text: "How to onboard to clusterfleet in Falcon?",
        value: "How to onboard to clusterfleet in Falcon?"
    },
    { text: "what is crossclusterdatadeployment in clusterfleet?", value: "what is crossclusterdatadeployment in clusterfleet?" },
    { text: "How to migrate to own keyvault from falcon shared keyvault?", value: "How to migrate to own keyvault from falcon shared keyvault?" }
];

interface Props {
    onExampleClicked: (value: string) => void;
}

export const ExampleList = ({ onExampleClicked }: Props) => {
    return (
        <ul className={styles.examplesNavList}>
            {EXAMPLES.map((x, i) => (
                <li key={i}>
                    <Example text={x.text} value={x.value} onClick={onExampleClicked} />
                </li>
            ))}
        </ul>
    );
};
