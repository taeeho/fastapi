import React from "react";

const ErrorMsg = ({ error }) => {
  if (!error) return null;

  return <p className="text-red-400 text-sm text-center">{error}</p>;
};

export default ErrorMsg ;