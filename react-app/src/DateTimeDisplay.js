import React, { useState, useEffect } from 'react';

const DateTimeDisplay = () => {
  const getCurrentDateTime = () => {
    const currentDateTime = new Date();

    const formattedDate =
      (currentDateTime.getMonth() + 1) +
      '/' +
      currentDateTime.getDate() +
      '/' +
      currentDateTime.getFullYear();

    const timeOptions = {
      hour: 'numeric',
      minute: '2-digit',
      second: '2-digit',
      hour12: true,
    };

    const formattedTime = currentDateTime.toLocaleTimeString(undefined, timeOptions);

    return formattedDate + ' ' + formattedTime;
  };

  const [dateTime, setDateTime] = useState(getCurrentDateTime());

  useEffect(() => {
    const intervalId = setInterval(() => {
      setDateTime(getCurrentDateTime());
    }, 1000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return <h3>{dateTime}</h3>;
};

export default DateTimeDisplay;
