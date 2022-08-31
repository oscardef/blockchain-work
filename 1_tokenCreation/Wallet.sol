// SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Wallet {
    address owner;

    mapping(IERC20 => mapping(address => uint256)) private _erc20Allowances;

    constructor() payable {
        owner = msg.sender;
    }

    function ethBalance() external view returns (uint) {
        return address(this).balance;
    }

    function erc20Balance(IERC20 token) external view returns (uint) {
        return token.balanceOf(address(this));
    }

    function sendERC20(IERC20 token, address to, uint256 amount) public {
        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance >= amount, "The wallet does not have this amount.");
        if (msg.sender != owner) {
            require(_erc20Allowances[token][msg.sender] >= amount, "You are not permitted to send this many tokens");
            _erc20Allowances[token][msg.sender] -= amount;
        }
        token.approve(address(this), amount);
        token.transferFrom(address(this), to, amount);
    }

    function sendEthToContract() public payable {
    }

    // allows contract to revieve ETH based on msg.value
    receive() external payable {}

    function sendEth(address payable to, uint amount) public payable {
        require(msg.sender == owner, "You are not the owner of this wallet.");
        (bool sent, bytes memory data) = to.call{value: amount}("");
        require(sent, "Failed to send Ether");
    }
    
    function setERC20Allowance(address spender, IERC20 token, uint amount) public {
        require(msg.sender == owner, "You are not the owner of this wallet.");
        _erc20Allowances[token][spender] = amount;
    }

    function getERC20Allowance(IERC20 token) external view returns (uint) {
        return _erc20Allowances[token][msg.sender];
    }
}