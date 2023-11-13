import React, { useState, useEffect } from 'react';

const AMZN = () => {
  const [price, setPrice] = useState('');
  const [info, setInfo] = useState('');
  const [graph1, setGraph1] = useState('');
  const [graph2, setGraph2] = useState('');

  useEffect(() => {
    const name = 'AMZN';
    const int_min = '1min';
    const int_day = '1day';

    const fetchData = async () => {
      try {
        const response_price = await fetch(`/stock_price/${name}`);
        const data_price = await response_price.text();

        const response_info = await fetch(`/stock_info/${name}`);
        const data_info = await response_info.text();

        const response_graph1 = await fetch(`/stock_graph/${name}/${int_min}`);
        const data_graph1 = await response_graph1.text();

        const response_graph2 = await fetch(`/stock_graph/${name}/${int_day}`);
        const data_graph2 = await response_graph2.text();

        if (data_info !== "Failed") {
          setInfo(data_info);
        }
        if (data_price !== "Failed" ) {
          setPrice(data_price);
        }
        if (data_graph1 !== "Failed" ) {
          setGraph1(data_graph1);
        }
        if (data_graph2 !== "Failed") {
          setGraph2(data_graph2);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    // Fetch data initially when the component mounts
    fetchData();

    // Set up an interval to fetch the data every minute
    const intervalId = setInterval(fetchData, 120000); // Run every 60 seconds (1 minute)

    // Clear the interval when the component is unmounted
    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div>
  <p dangerouslySetInnerHTML={{ __html: info === '' ? 'Loading Info...' : info }}></p>
  <p dangerouslySetInnerHTML={{ __html: price === '' ? 'Loading Price...' : price }}></p>
  <img src={`data:image/png;base64,${graph1 === '' ? 'Loading Graph 1...' : graph1}`} alt="Graph by Minute" />
  <img src={`data:image/png;base64,${graph2 === '' ? 'Loading Graph 2...' : graph2}`} alt="Graph by Day" />
</div>
  );
};

export default AMZN;
