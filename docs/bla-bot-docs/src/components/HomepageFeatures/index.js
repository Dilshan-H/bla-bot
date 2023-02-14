import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Easy to Use & Customize',
    image: require('@site/static/img/1.png').default,
    description: (
      <>
        The bot is easy to use and understand. You can add BLA-BOT to your academic group 
        and easily provide information to your fellow students.
      </>
    ),
  },
  {
    title: 'You are in Control',
    image: require('@site/static/img/2.png').default,
    description: (
      <>
        The bot is secure and private. Users only see the data they are authorized to see. 
        Unauthorized access alerts, admin commands, and more.
      </>
    ),
  },
  {
    title: 'Well Documented',
    image: require('@site/static/img/3.png').default,
    description: (
      <>
        The bot is well documented and has a detailed instructions. You can easily understand 
        how the bot works and how to customize it according to your needs.
      </>
    ),
  },
];

function Feature({image, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <img className={styles.featureSvg} src={image} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
