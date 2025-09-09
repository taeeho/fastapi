import React from "react";
import { BiSearch } from "react-icons/bi";

const MobileMenu = ({
  isOpen,
}) => {
  return (
    <div
      className={`md:hidden transform transition-all duration-500 ease-in-out ${
        isOpen
          ? "opacity-100 translate-y-0 bg-purple-500"
          : "opacity-0 -translate-y-2 pointer-events-none h-0 overflow-hidden"
      }`}
    >
      <div>테스트1</div>
      <div>테스트2</div>
      <div>테스트3</div>
      <div>테스트4</div>
    </div>
  );
};
export default MobileMenu;